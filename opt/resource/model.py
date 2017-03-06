from concourse_common import common

VERSION_JSON_NAME = 'version'


class Model:

    def __init__(self):
        self.payload = common.load_payload()

    def get_version_file(self):
        version = self.payload['params']['version']
        return version

    def get_command(self):
        command = self.payload['params']['command']
        return command

    def get_slack_bot_token(self):
        token = self.payload['params']['SLACK_BOT_TOKEN']
        return token

    def get_slack_channel(self):
        channel = self.payload['params']['channel']
        return channel

    def get_pipeline_step(self):
        step = self.payload['params']['pipeline_step']
        return step

    def get_directory(self):
        directory = self.payload['params']['directory']
        return directory

    def get_version(self):
        version = self.payload['version']['version']
        return version