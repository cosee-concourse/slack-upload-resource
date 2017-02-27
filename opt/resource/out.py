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

    sc.api_call("chat.postMessage", token=model.get_slack_bot_token(),
                channel=model.get_slack_channel(),
                text="Here are the latest JUnit Test Reports:")

    for file in os.listdir(os.path.join(filepath, model.get_directory())):
        if file.endswith(".html"):

            sc.api_call("files.upload", content=open(os.path.join(filepath, model.get_directory(), file)).read(),
                        channels=model.get_slack_channel(),
                        title=open(os.path.join(filepath, model.get_version_file())).read() + "-" + file,
                        filename=open(os.path.join(filepath, model.get_version_file())).read() + "-" + file)

    common.log("uploaded file to slack")

    print(json.dumps({"version": {"version": open(os.path.join(filepath, model.get_version_file())).read()}}))

    return 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))