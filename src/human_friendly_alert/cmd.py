# coding: utf-8

import click


@click.group()
def cmd():
    pass

@cmd.command()
def alert():
    click.echo('Hello world')

def main():
    cmd()

if __name__ == '__main__':
    main()

