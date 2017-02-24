import sys
from concourse_common import common
import json
from model import Model


def execute():

    try:
        model = Model()
    except:
        return -1

    print(json.dumps({"version": {"version": model.get_version()}}))

    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute())