import re
import yaml
from .AceLayer import AceLayer
from .customagents.l6prosecution.TaskProsecution import TaskProsecution


class L6Prosecution(AceLayer):

    def initialize_agents(self):
        self.agent = TaskProsecution()

    def parse_agent_output(self):
        self.interface.handle_south_bus(self.parsed_result)
