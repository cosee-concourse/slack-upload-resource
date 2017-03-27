import unittest
import json
import out
from concourse_common import testutil


class TestOutput(unittest.TestCase):

    def test_json_output_wrong_command(self):
        testutil.put_stdin(json.dumps({"source": {"SLACK_BOT_TOKEN": "test"}, "params": {"version": "1.1.0",
                                                                                         "command": "1.1.0",
                                                                                         "channel": "sdfswfew",
                                                                                         "directory": "1.1.0"}}))
        self.assertEquals(out.execute("/"), -1)

if __name__ == '__main__':
    unittest.main()