import sys
from concourse_common import common
import json
from model import Model
from slackclient import SlackClient
import os
import xml.etree.ElementTree


def build_total_string(dict):
    result = "tests" + ": " + str(dict["tests"]) + " "
    result = result + "errors" + ": " + str(dict["errors"]) + " "
    result = result + "skipped" + ": " + str(dict["skipped"]) + " "
    result = result + "failures" + ": " + str(dict["failures"]) + " "
    return result


def list_tests(dict):
    result = ""
    for key in dict:
        result = result + key + " in " + dict[key] + "\n\n"
    return result


def execute(filepath):

    try:
        model = Model()
    except:
        return -1

    sc = SlackClient(model.get_slack_bot_token())

    if model.get_command() == "report":

        count = {"tests": 0, "errors": 0, "skipped": 0, "failures": 0}
        failed = {}
        for file in os.listdir(os.path.join(filepath, model.get_directory())):
            if file.endswith(".xml"):
                current_file = os.path.join(filepath, model.get_directory(), file)
                root = xml.etree.ElementTree.parse(current_file).getroot()
                for key in count.keys():
                    count[key] += int(root.attrib[key])

                for testcase in root.findall("testcase"):
                    for child in testcase:
                        common.log(child.tag)
                        if child.tag == "failure":
                            failed[testcase.attrib["name"]] = testcase.attrib["classname"]
                            common.log(testcase.attrib["name"] + " in " + testcase.attrib["classname"])

        total_string = build_total_string(count)
        common.log(total_string)
        failed_string = list_tests(failed)
        common.log(failed_string)

        if count["failures"] > 0:

            sc.api_call("chat.postMessage", as_user=True,
                        channel=model.get_slack_channel(), attachments=[{"fallback": "Test Results",
                                                                         "pretext": "Here are latest test results:",
                                                                         "color": "danger",
                                                                         "text": total_string,
                                                                         "title": "Test Results",
                                                                         "fields": [{"title": "Failures: ",
                                                                                     "value": failed_string,
                                                                                     "short": False}]}])

        else:

            sc.api_call("chat.postMessage", as_user=True,
                        channel=model.get_slack_channel(), attachments=[{"fallback": "Test Results",
                                                                         "pretext": "Here are latest test results:",
                                                                         "color": "good",
                                                                         "title": "Test Results: ",
                                                                         "fields": [{"value": total_string,
                                                                                     "short": False}]}])

    common.log("uploaded file to slack")

    print(json.dumps({"version": {"version": open(os.path.join(filepath, model.get_version_file())).read()}}))

    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))

