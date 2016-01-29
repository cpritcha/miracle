#!/usr/bin/env python

import os
import sys


def writeenvs(in_path, out_path, default):
    with open(out_path, "a") as g:
        with open(in_path) as f:
            contents = f.readlines()
            for line in contents:
                line = line.strip()
                if len(line) > 0 and line[-1] == "=":
                    line += default
                if line:
                    g.write("\nexport {}".format(line))

# Do not change this without ensuring the file is ignored by git
OUT_PATH="source.sh"
DEV_ENV_FILES = ["base/db.env",
                 "base/deployr.env",
                 "base/django.env",
                 "dev/django.env",
                 "dev/db.env"]
TRAVIS_ENV_FILES = ["base/db.env",
                    "base/deployr.env.example",
                    "base/django.env.example",
                    "dev/django.env",
                    "dev/db.env.example"]

def writeparams(setting):
    if setting == "dev":
        files = DEV_ENV_FILES
        default = ""
    elif setting == "travis":
        files = TRAVIS_ENV_FILES
        default = "CHANGEME"
    else:
        raise ValueError("argument '{}' invalid. Must be one of 'dev' or 'travis'")
    with open(OUT_PATH, "w") as f:
        f.truncate()
        f.write("#!/usr/bin/env bash\n")
    os.chmod(OUT_PATH, 0o711)
    for in_path in files:
        writeenvs(in_path, OUT_PATH, default)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("must have exactly one argument")

    setting = sys.argv[1]
    writeparams(setting)


