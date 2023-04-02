import logging

import os
import sys
import types
from pathlib import Path

path, tail = os.path.split(__file__)
os.chdir(path)


def import_parents(level):
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[level]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError:
        pass

    __package__ = '.'.join(parent.parts[len(top.parts):])


def print_import(string):
    print(string)
    for name, val in list(globals().items()):
        if isinstance(val, types.ModuleType):
            name = val.__name__
            print("Main -", name)


import_parents(1)

from src.discord.discord_module import DiscordBot

if __name__ == '__main__':
    logging.info('Inizio esecuzione programma')
    try:

        DiscordBot().start_bot()
        pass
    except Exception as e:
        logging.error(f'Errore durante l\'esecuzione del programma: {e}')
    finally:
        logging.info('Fine esecuzione programma')
