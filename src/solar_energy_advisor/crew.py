from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# Defining the crew using the CrewBase decorator
@CrewBase
class SolarEnergyAdvisor():
    """SolarEnergyAdvisor crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

# defining the agents using the @agent decorator
    @agent
    def energy_needs_assessor(self) -> Agent:
        return Agent(
            config=self.agents_config['energy_needs_assessor'], # type: ignore[index]
            verbose=True
        )

    @agent
    def solar_system_recommender(self) -> Agent:
        return Agent(
            config=self.agents_config['solar_system_recommender'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def cost_financing_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['cost_financing_advisor'], # type: ignore[index]
            verbose=True
        )
    
    # @agent
    # def implementation_planner(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['implementation_planner'], # type: ignore[index]
    #         verbose=True
    #     )
    
    @agent
    def solar_report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['solar_report_generator'], # type: ignore[index]
            verbose=True
        )

    # Defining the tasks using the @task decorator
    @task
    def assess_energy_needs_task(self) -> Task:
        return Task(
            config=self.tasks_config['assess_energy_needs_task'], # type: ignore[index]
        )
    
    @task
    def recommend_solar_system_task(self) -> Task:
        return Task(
            config=self.tasks_config['recommend_solar_system_task'], # type: ignore[index]
        )
    
    @task
    def calculate_costs_task(self) -> Task:
        return Task(
            config=self.tasks_config['calculate_costs_task'], # type: ignore[index]
        )

    @task
    def generate_solar_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_solar_report_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SolarEnergyAdvisor crew"""
    

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
