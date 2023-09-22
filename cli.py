#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Console script for sncli."""
import click
import os
import inspect
import sys
import shutil
import datetime
from pathlib import Path

PLUGIN_FOLDER = os.path.join(os.path.dirname(__file__), "plugins")
HOMEDIR = Path.home()

TODAY = datetime.date.today().strftime("%Y-%m-%d")
ISODATE = datetime.date.today().strftime("%Y-%m-%d")
ISOFILE = ISODATE + ".md"
BUJO_FOLDER = os.path.join(os.path.dirname(__file__), "docs/bujo")
MONTH = datetime.date.today().strftime("%m_%B")
WEEK = datetime.date.today().strftime("%U")
DAYFILE = BUJO_FOLDER + "/" + TODAY + ".md"
WEEKFILE = BUJO_FOLDER + "/" + WEEK + ".md"
MONTHFILE = BUJO_FOLDER + MONTH + ".md"
YEAR = datetime.date.today().strftime("%Y")


class PluginCLI(click.MultiCommand):
    def list_commands(self, ctx):
        """Dynamically get the list of commands."""
        rv = []
        for filename in os.listdir(PLUGIN_FOLDER):
            if filename.endswith(".py") and not filename.startswith("__init__"):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """Dynamically get the command."""
        ns = {}
        fn = os.path.join(PLUGIN_FOLDER, name + ".py")
        with open(fn) as f:
            code = compile(f.read(), fn, "exec")
            eval(code, ns, ns)
        return ns["cli"]


@click.command(cls=PluginCLI)
def cli():
    """2022 Shane Null Workflows"""
    #    click.echo(dir(PluginCLI))
    pass


if __name__ == "__main__":
    cli()
