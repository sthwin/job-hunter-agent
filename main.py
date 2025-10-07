from crewai import Crew, Agent, Task
from crewai.project import CrewBase, task, agent, crew
from typing import List
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

from models import ChosenJob, JobList, RankedJob, RankedJobList
from tools import web_search_tool


def create_resume_knowledge(name: str):
    return TextFileKnowledgeSource(
        collection_name=name,
        file_paths=["resume.txt"],
    )


@CrewBase
class JobHunterCrew:

    agents: List[BaseAgent]
    tasks: List[Task]

    # Paths to your YAML configuration files
    # To see an example agent and task defined in YAML, checkout the following:
    # - Task: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    # - Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def job_search_agent(self) -> BaseAgent:
        return Agent(
            config=self.agents_config["job_search_agent"],
            tools=[web_search_tool],
        )

    @agent
    def job_matching_agent(self) -> BaseAgent:
        return Agent(
            config=self.agents_config["job_matching_agent"],
            knowledge_sources=[
                create_resume_knowledge("job_matching_agent_resume_knowledge")
            ],
        )

    @agent
    def resume_optimization_agent(self) -> BaseAgent:
        return Agent(
            config=self.agents_config["resume_optimization_agent"],
            knowledge_sources=[
                create_resume_knowledge("resume_optimization_agent_resume_knowledge")
            ],
        )

    @agent
    def company_research_agent(self) -> BaseAgent:
        return Agent(
            config=self.agents_config["company_research_agent"],
            knowledge_sources=[
                create_resume_knowledge("company_research_agent_resume_knowledge")
            ],
            tools=[web_search_tool],
        )

    @agent
    def interview_prep_agent(self) -> BaseAgent:
        return Agent(
            config=self.agents_config["interview_prep_agent"],
            knowledge_sources=[
                create_resume_knowledge("interview_prep_agent_resume_knowledge")
            ],
        )

    @task
    def job_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_extraction_task"],
            output_pydantic=JobList,
        )

    @task
    def job_matching_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_matching_task"],
            output_pydantic=RankedJobList,
        )

    @task
    def job_selection_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_selection_task"],
            output_pydantic=ChosenJob,
        )

    @task
    def resume_rewriting_task(self) -> Task:
        return Task(
            config=self.tasks_config["resume_rewriting_task"],
            context=[
                self.job_selection_task(),
            ],
        )

    @task
    def company_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["company_research_task"],
            context=[
                self.job_selection_task(),
            ],
        )

    @task
    def interview_prep_task(self) -> Task:
        return Task(
            config=self.tasks_config["interview_prep_task"],
            context=[
                self.job_selection_task(),
                self.resume_rewriting_task(),
                self.company_research_task(),
            ],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )


result = (
    JobHunterCrew()
    .crew()
    .kickoff(
        inputs={
            "level": "Senior",
            "position": "Golang Developer",
            "location": "Netherlands",
        },
    )
)

for task_output in result.tasks_output:
    print(task_output.pydantic)
