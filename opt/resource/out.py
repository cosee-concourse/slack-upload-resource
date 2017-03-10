import sys
from concourse_common import common
import json
from model import Model
from slackclient import SlackClient
import os
import xml.etree.ElementTree
import slack_post


def execute(filepath):

    try:
        model = Model()
    except:
        return -1

    sc = SlackClient(model.get_slack_bot_token())

    if model.get_command() == "failure":
        slack_post.post_failure_message(filepath, model, sc)

    if model.get_command() == "success":
        slack_post.post_success_message(filepath, model, sc)

    if model.get_command() == "report":

        count = {"tests": 0, "errors": 0, "skipped": 0, "failures": 0}
        failed = {}
        for file in os.listdir(os.path.join(filepath, model.get_directory())):
            if file.endswith(".xml"):
                current_file = os.path.join(filepath, model.get_directory(), file)
                root = xml.etree.ElementTree.parse(current_file).getroot()
                for key in count.keys():
                    count[key] += int(root.attrib[key])

                extract_failed_tests(failed, root)

        total_string = build_total_string(count)
        common.log(total_string)
        failed_string = list_tests(failed)
        common.log(failed_string)

        if count["failures"] > 0:

            slack_post.post_failed_tests(failed_string, filepath, model, sc, total_string)

        else:

            slack_post.post_successful_tests(filepath, model, sc, total_string)

    print(json.dumps({"version": {"version": open(os.path.join(filepath, model.get_version_file())).read()}}))

    return 0


def extract_failed_tests(failed, root):
    for testcase in root.findall("testcase"):
        for child in testcase:
            common.log(child.tag)
            if child.tag == "failure":
                failed[testcase.attrib["name"]] = testcase.attrib["classname"]
                common.log(testcase.attrib["name"] + " in " + testcase.attrib["classname"])


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

if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))

