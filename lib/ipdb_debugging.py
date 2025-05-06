#!/usr/bin/env python3

import ipdb_debugging as ipdb

def plus_two(num):
    ipdb.set_trace()  # Debugging breakpoint
    num += 2
    return num
