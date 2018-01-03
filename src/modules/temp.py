#!/bin/python

# As of now, Shadow Suite cannot install modules automatically.
# To manually install a module, see README-DEV file and find
# 'Manually installing a module'.

def main(): 
    # import modules here
    import os
    import sys
    import core.misc
    import core.error

    try:
        module_name = "Module Name" # Insert Module name here.
        module_version = "v1.0" # Insert module version here.
        module_desc = "Module description." # Insert module brief description here.

        print(module_name + "\n" + module_version + "\n" + module_desc)
        #write your module here.

    except KeyboardInterrupt:
        core.error.error0002()
