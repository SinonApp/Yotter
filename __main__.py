import argparse
import shutil
import os
from pathlib import Path
from distutils.dir_util import copy_tree

BASE_DIR = Path(__file__).resolve().parent

parser = argparse.ArgumentParser(prog = 'manage.py', description = 'Manager for Yotter')
parser.add_argument('command')
parser.add_argument('name')
args = parser.parse_args()

if args.command == 'startproject':
    #os.mkdir(f'./{args.name}')
    copy_tree(BASE_DIR / 'templates/project/', f'./{args.name}/')