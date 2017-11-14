# coding: utf-8

import sys
from os.path import dirname
from logging import getLogger, StreamHandler, DEBUG

from flask import Flask
import click

handler = StreamHandler(sys.stdout)
logger = getLogger(dirname(__name__))
logger.propagate = False
logger.addHandler(handler)

app = Flask(__name__)


@click.group()
def cmd():
    pass

@cmd.command()
def alert():
    click.echo('Hello world')

@cmd.command()
@click.option('--debug', is_flag=True, default=True)
@click.option('--port', type=int, default='8000')
@click.option('--host', default='0.0.0.0')
def runserver(host, port, debug):
    if debug:
        app.debug = True
        handler.setLevel(DEBUG)
        logger.setLevel(DEBUG)
    app.run(host=host, port=port)

def main():
    cmd()

if __name__ == '__main__':
    main()

