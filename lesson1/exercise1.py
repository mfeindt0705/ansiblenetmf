#!/usr/bin/env python3
"""
exercise 1  lesson 1
read yml file and print file out
"""

import yaml
from pprint import pprint

filename = "liste.yml"

with open(filename, 'r') as f:
    vliste = yaml.load(f)

pprint(vliste)


