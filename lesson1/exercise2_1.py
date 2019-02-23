#!/usr/bin/env python3
"""
define base functions for yaml file
read-file and write_file
"""

# !/usr/bin/env python3
"""
def basic functions for yaml processing
"""

import yaml
from pprint import pprint

def read_yaml(filename):
    """
    yaml file processing
    function has filename as input and returns the file data processed by yaml
    """
    with open(filename, 'r') as f:
        return yaml.load(f)


def write_yaml(vdata, filename):
    """
    yaml file processing
    function has data structure and filename as input
    data is written to file filename as a yaml formatted file
    """
    return None


if __name__ == "__main__":
    filename = input("Bitte geben Sie den Dateinamen ein : ")
    vdata = read_yaml(filename)
    pprint(vdata)

