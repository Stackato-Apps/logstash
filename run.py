#!/usr/bin/env python

import os
import json
import subprocess

services = json.loads(os.environ['STACKATO_SERVICES'])

host = str(services['search']['host'])
port = str(services['search']['port'])

def inline_replace(old, new, file):
    f1 = open(file, 'r')
    f2 = open(file + '.tmp', 'w')
    for line in f1:
        f2.write(line.replace(old, new))
    f1.close()
    f2.close()
    f1 = open(file, 'w')
    f2 = open(file + '.tmp', 'r')
    for line in f2:
        f1.write(line)
    f1.close()
    f2.close()

if __name__ == "__main__":
    inline_replace('localhost', host, 'logstash.conf')
    inline_replace('9200', port, 'logstash.conf')
    inline_replace('9200', port, 'kibana/config.js')
