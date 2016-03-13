import argparse
import os
import sys

def is_valid_folder(parser, directory):
	if not os.path.exists(directory):
		parser.error("%s does not exist" %directory)
		return False
	if os.path.isfile(directory):
		parser.error("%s is not a directory" %directory)
		return False
	return True

def put_description(directory, message=''):
	try:
		target = open(directory + '/.aboutdir', 'w')
		target.truncate()
		if message=='':
			print 'Enter description : '
			msg = raw_input()
		else:
			msg = message
		target.write(msg)
		target.close()
	except:
		print 'There was an unexpected error while storing description'
		exit(0)


def get_description(directory):
	try:
		target = open(directory + '/.aboutdir', 'r')
		contents = target.read()
		target.close()
		return contents
	except:
		print 'There was an unexpected error while retrieving description'
		exit(0)
	
def delete_description(directory):
	try:
		os.remove(directory+ '/.aboutdir')
	except:
		print 'Error deleting'
		exit(0)

def main():
	parser = argparse.ArgumentParser(description='Add description to folders')

	parser.add_argument("directory", help="Directory you wish to see description for")
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-m', '--description', type=str, help='Add description to the directory')
	group.add_argument('-d', '--delete', action='store_true', help='Delete description for the directory')

	if len(sys.argv) == 1:
		parser.print_help()
		return

	args = parser.parse_args()

	directory = args.directory
	if not is_valid_folder(parser,args.directory):
		exit(0)

	if args.description:
		put_description(directory, args.description)
		print 'Successfully updated description'
		exit(0)

	if args.delete:
		if not os.path.exists(directory + '/.aboutdir'):
			print 'No description to delete'
			exit(0)
		print 'Are you sure to delete description for '+directory+'? (y/N)'
		y = raw_input()
		if y=='y':
			delete_description(directory)
		exit(0)

	if os.path.exists(directory + '/.aboutdir'):
		print 'Description for '+ directory
		print get_description(directory)

	else:
		print "No description yet. Do you want to add one? (y/N)"
		y = raw_input()
		if y=='y':
			put_description(directory)
		exit(0)
