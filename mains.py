import argparse
import os

parser = argparse.ArgumentParser(description='Add description to folders')

parser.add_argument("directory", help="Enter the directory you wish to add/see description for")

args = parser.parse_args()

def is_valid_folder(parser, directory):
	if not os.path.exists(directory):
		parser.error("%s does not exist" %directory)
	if os.path.isfile(directory):
		parser.error("%s is not a directory" %directory)

is_valid_folder(parser,args.directory)