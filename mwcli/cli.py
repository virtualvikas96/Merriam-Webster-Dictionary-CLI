import argparse
from mwcli.api import fetch_definitions
from mwcli.formatter import format_definition

def main():
    parser = argparse.ArgumentParser(description="Merriam-Webster Dictionary CLI")
    parser.add_argument("word", help="The word to define")
    args = parser.parse_args()

    entries = fetch_definitions(args.word)
    print(format_definition(args.word, entries))

