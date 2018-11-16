#! python3
# main.py

import sys, re, os
import argparse
from rename import *

def run():
	paser = argparse.ArgumentParser(
		prog='mr',
		description='batch renaming files under a specified path'
	)
	paser.add_argument(
		'-p',
		'--path',
		nargs=1,
		help='specify path'
	)
	paser.add_argument(
		'-pre',
		'--prefix',
		nargs=1,
		help='specify file prefix'
	)
	paser.add_argument(
		'-suf',
		'--suffix',
		nargs=1,
		help='specify file suffix'
	)
	paser.add_argument(
		'-1',
		action='store_true',
		dest='is_one',
		default=False,
		help="use regex text '\D?(\d{1,2})'"
	)
	paser.add_argument(
		'-2',
		action='store_true',
		dest='is_two',
		default=False,
		help="use regex text '.*[eE](\d{1,2})'"
	)
	paser.add_argument(
		'-e',
		'--regex',
		nargs=1,
		help='specify regex'
	)
	paser.add_argument(
		'-L',
		'--last',
		action='store_true',
		dest='is_last',
		default=False,
		help='use the last renaming method'
	)
	paser.add_argument(
		'-c',
		'--cat',
		action='store_true',
		dest='is_cat',
		default=False,
		help='show information that the last renaming methods'
	)
	paser.add_argument(
		'-d',
		'--delete',
		nargs=1,
		help='delete words in filename, the argument required: -p/--path'
	)
	args = paser.parse_args()

	if args.delete and args.path:
		deleteWords(args.path[0], args.delete[0])

	if args.is_cat:
		ar = last()
		for n in ar:
			print(n)
		print('')
		sys.exit()

	if args.is_last:
		ar = last()
		filenames = show_rename_files()
		Rename(filenames, ar[1], ar[2], ar[3])
	else:
		ar = init(args)
		filenames = show_rename_files()
		Rename(filenames, ar[1], ar[2], ar[3])

if __name__ == '__main__':
	run()