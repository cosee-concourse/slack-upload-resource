from concourse_common import common

VERSION_JSON_NAME = 'version'


class Model:

    def __init__(self):
        self.payload = common.get_payload()

    def get_version_file(self):
        version = self.payload['params']['version']
        return version

    def get_slack_bot_token(self):
        version = self.payload['params']['SLACK_BOT_TOKEN']
        return version

    def get_directory(self):
        version = self.payload['params']['directory']
        return version

    def get_version(self):
        version = self.payload['version']['version']
        return version