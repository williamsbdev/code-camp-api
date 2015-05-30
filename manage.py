#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    settings_file = 'production'
    args = sys.argv
    if sys.argv[1] == 'test':
        settings_file = 'test'
        args = [sys.argv[0]] + sys.argv[2:]
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.{}".format(settings_file))
    from django.core.management import execute_from_command_line
    execute_from_command_line(args)
