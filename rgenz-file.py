# v0.0.2 sept 3 2022

import os
import sys
import json
import argparse
from pathlib import Path

file = open('config.json')
config = json.loads(file.read())
tracker = config['tracker']
ss_num = config['ss_number']
ss_gap = config['ss_gap']
pic_ext = config['pic_ext']

parser = argparse.ArgumentParser()
parser.add_argument(dest='single_file', nargs='?',
                    help='Video file to make a torrent off.')
args = parser.parse_args()

file_path = Path(args.single_file)
dir_only = os.path.dirname(args.single_file)
file_name = os.path.basename(file_path).split('/')[-1]

print("\nv0.0.2\n"
      "_______  ______ _______ __   _  _____\n"
      "|_____/ |  ____ |______ | \  |  ____/\n"
      "|    \_ |_____| |______ |  \_| /_____\n\n"
      "     r3n generic torrent helper\n"
      )


def start(arg):
    if file_path == None:
        print('No file provided. Try again.')
        sys.exit()
    else:
        take_screens()
        create_torrent()
        mediainfo()


def take_screens():
    print('Generating screenshots..')
    os.system(f'''ffmpeg -nostats -loglevel 0 -i "{file_path}" -vf "select='not(mod(n,{ss_gap}))',setpts='N/(30*TB)'" -f image2 -frames:v {ss_num} "{dir_only}\\RGENZ_screens_%03d_{file_name}{pic_ext}"''')


def create_torrent():
    print('Creating torrent file..')
    os.system(
        f'py3createtorrent "{file_path}" -t "{tracker.strip()}" -P -q -o "{dir_only}\\[RGENZ]_{file_name}.torrent"')


def mediainfo():
    print('Generating mediainfo...\n')
    os.system(
        f'mediainfo --LogFile="{dir_only}\\{file_name}.txt" "{file_path}"')


start(file_path)
print("Done!")
