import sys
from concourse_common import common
import json
from model import Model
from slackclient import SlackClient
import os


def execute(filepath):

    try:
        model = Model()
    except:
        return -1

    sc = SlackClient(model.get_slack_bot_token())

    for file in os.listdir(os.path.join(filepath, model.get_directory())):
        if file.endswith(".html"):

            sc.api_call("files.upload", content=open(os.path.join(filepath, model.get_directory(), file)).read(),
                        channels="bot-test", title=file + open(os.path.join(filepath, model.get_version_file())).read(),
                        filename=file + open(os.path.join(filepath, model.get_version_file())).read())

    common.log("uploaded file to slack")

    print(json.dumps({"version": {"version": open(os.path.join(filepath, model.get_version_file())).read()}}))

    return 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))