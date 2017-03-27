import os
from concourse_common import jsonutil


def post_successful_tests(filepath, payload, sc, total_string):
    sc.api_call("chat.postMessage", as_user=True,
                channel=jsonutil.get_params_value(payload, "channel"),
                attachments=[{"fallback": "Test Results",
                              "pretext": "Test results of " + os.environ["BUILD_JOB_NAME"] + " in version " + open(
                                  os.path.join(filepath, jsonutil.get_params_value(payload, "version"))).read(),
                              "color": "good",
                              "title": "Test Results: ",
                              "fields": [{"value": total_string,
                                          "short": False}]}])


def post_failed_tests(failed_string, filepath, payload, sc, total_string):
    sc.api_call("chat.postMessage", as_user=True,
                channel=jsonutil.get_params_value(payload, "channel"),
                attachments=[{"fallback": "Test Results",
                              "pretext": "Test results of " + os.environ["BUILD_JOB_NAME"] + " in version " + open(
                                  os.path.join(filepath, jsonutil.get_params_value(payload, "version"))).read(),
                              "color": "danger",
                              "text": total_string,
                              "title": "Test Results",
                              "fields": [{"title": "Failures: ",
                                          "value": failed_string,
                                          "short": False}]}])


def post_success_message(filepath, payload, sc):
    sc.api_call("chat.postMessage", as_user=True,
                channel=jsonutil.get_params_value(payload, "channel"),
                attachments=[{"fallback": "Pipeline Success of version " + open(
                    os.path.join(filepath, jsonutil.get_params_value(payload, "version"))).read(),
                              "pretext": "Pipeline Success",
                              "color": "good",
                              "title": "Success:",
                              "fields": [
                                  {"value": "Version " + open(os.path.join(filepath,
                                            jsonutil.get_params_value(payload, "version"))).read() +
                                            " successfully finished the Pipeline with Job: " +
                                            os.environ["BUILD_JOB_NAME"],
                                            "short": False}]}])


def post_failure_message(filepath, payload, sc):
    sc.api_call("chat.postMessage", as_user=True,
                channel=jsonutil.get_params_value(payload, "channel"),
                attachments=[{"fallback": "Pipeline Failure in " + jsonutil.get_params_value(payload, "pipeline_step"),
                              "pretext": "Pipeline Failure",
                              "color": "danger",
                              "title": "Failure:",
                              "fields": [{"value": os.environ["BUILD_JOB_NAME"] + " in version " + open(
                                  os.path.join(filepath, jsonutil.get_params_value(payload, "version"))).read() + "failed",
                                          "short": False}]}])