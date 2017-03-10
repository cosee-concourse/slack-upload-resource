import os


def post_successful_tests(filepath, model, sc, total_string):
    sc.api_call("chat.postMessage", as_user=True,
                channel=model.get_slack_channel(),
                attachments=[{"fallback": "Test Results",
                              "pretext": "Test results of " + model.get_pipeline_step() + " in version " + open(
                                  os.path.join(filepath, model.get_version_file())).read(),
                              "color": "good",
                              "title": "Test Results: ",
                              "fields": [{"value": total_string,
                                          "short": False}]}])


def post_failed_tests(failed_string, filepath, model, sc, total_string):
    sc.api_call("chat.postMessage", as_user=True,
                channel=model.get_slack_channel(),
                attachments=[{"fallback": "Test Results",
                              "pretext": "Test results of " + model.get_pipeline_step() + " in version " + open(
                                  os.path.join(filepath, model.get_version_file())).read(),
                              "color": "danger",
                              "text": total_string,
                              "title": "Test Results",
                              "fields": [{"title": "Failures: ",
                                          "value": failed_string,
                                          "short": False}]}])


def post_success_message(filepath, model, sc):
    sc.api_call("chat.postMessage", as_user=True,
                channel=model.get_slack_channel(),
                attachments=[{"fallback": "Pipeline Success of version " + open(
                    os.path.join(filepath, model.get_version_file())).read(),
                              "pretext": "Pipeline Success",
                              "color": "good",
                              "title": "Success:",
                              "fields": [
                                  {"value": "Version " + open(os.path.join(filepath,
                                                                           model.get_version_file())).read() + " successfully finished the Pipeline",
                                   "short": False}]}])


def post_failure_message(filepath, model, sc):
    sc.api_call("chat.postMessage", as_user=True,
                channel=model.get_slack_channel(),
                attachments=[{"fallback": "Pipeline Failure in " + model.get_pipeline_step(),
                              "pretext": "Pipeline Failure",
                              "color": "danger",
                              "title": "Failure:",
                              "fields": [{"value": model.get_pipeline_step() + " in version " + open(
                                  os.path.join(filepath, model.get_version_file())).read() + "failed",
                                          "short": False}]}])