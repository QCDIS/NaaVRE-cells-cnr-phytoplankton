
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_word = os.getenv('secret_word')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--names', action='store', type=str, required=True, dest='names')


args = arg_parser.parse_args()
print(args)

id = args.id

names = json.loads(args.names)



for name in names:
  print(f"Hello, {name}! This is the secret word: {secret_word}")

