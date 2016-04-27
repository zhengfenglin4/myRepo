#!/usr/bin/env python
import re
import sys
args = sys.argv
ACTIONS = re.sub(r'\s','',args[1]).split(':',1)[1]
print ACTIONS
