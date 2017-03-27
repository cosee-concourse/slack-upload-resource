import unittest
import json
import out
from concourse_common import testutil
from unittest.mock import patch


class TestOutput(unittest.TestCase):

    def test_json_output_wrong_command(self):
        testutil.put_stdin(json.dumps({"source": {"SLACK_BOT_TOKEN": "test"}, "params": {"version": "1.1.0",
                                                                                         "command": "1.1.0",
                                                                                         "channel": "reports",
                                                                                         "directory": "1.1.0"}}))
        self.assertEquals(out.execute("/"), -1)

    @patch("out.open")
    @patch("out.json")
    @patch("out.slack_post")
    def test_correct_slack_method_was_called(self, mock_io, mock2, mock3):
        testutil.put_stdin(json.dumps({"source": {"SLACK_BOT_TOKEN": "test"}, "params": {"version": "1.1.0",
                                                                                         "command": "success",
                                                                                         "channel": "reports"}}))
        out.execute("/")
        mock_io.post_success_message.assert_called_with(unittest.mock.ANY, unittest.mock.ANY, unittest.mock.ANY)

    @patch("out.open")
    @patch("out.json")
    @patch("out.slack_post")
    def test_correct_slack_failure_method_was_called(self, mock_io, mock2, mock3):
        testutil.put_stdin(json.dumps({"source": {"SLACK_BOT_TOKEN": "test"}, "params": {"version": "1.1.0",
                                                                                         "command": "failure",
                                                                                         "channel": "reports"}}))
        out.execute("/")
        mock_io.post_failure_message.assert_called_with(unittest.mock.ANY, unittest.mock.ANY, unittest.mock.ANY)


if __name__ == '__main__':
    unittest.main()