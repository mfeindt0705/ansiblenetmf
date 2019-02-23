#!/usr/bin/env python3
"""
exercise 2
"""

import yaml
from pprint import pprint

filename = "dict.yml"

with open(filename, 'r') as f:
   vdict = yaml.load(f)

pprint(vdict)


