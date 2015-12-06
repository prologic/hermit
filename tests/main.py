#!/usr/bin/env python

import sys
from types import ModuleType
from os.path import abspath, dirname
from subprocess import Popen, STDOUT


def importable(module):
    try:
        m = __import__(module, globals(), locals())
        return isinstance(m, ModuleType)
    except ImportError:
        return False


def main():
    cmd = ["py.test", "-s", "-r", "fsxXE", "--ignore=tmp", "--durations=10"]

    if importable("pytest_cov"):
        cmd.append("--cov=hermit")
        cmd.append("--cov-report=html")

    cmd.append(dirname(abspath(__file__)))

    raise SystemExit(Popen(cmd, stdout=sys.stdout, stderr=STDOUT).wait())


if __name__ == "__main__":
    main()