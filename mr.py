#! python3
# main.py

import sys, re, os
import argparse
from rename import *

def run():
	parse = argparse.ArgumentParser(
		prog='mr',
		description='batch renaming files under a specified path'
	)
	parse.add_argument(
		'-p',
		'--path',
		nargs=1,
		help='specify path'
	)
	parse.add_argument(
		'-pre',
		'--prefix',
		nargs=1,
		help='specify file prefix'
	)
	parse.add_argument(
		'-suf',
		'--suffix',
		nargs=1,
        default=[''],
		help='specify file suffix'
	)
	parse.add_argument(
		'-1',
		action='store_true',
		dest='is_one',
		default=False,
		help="use regex text '\D?(\d{1,2})'"
	)
	parse.add_argument(
		'-2',
		action='store_true',
		dest='is_two',
		default=False,
		help="use regex text '.*[eE](\d{1,2})'"
	)
	parse.add_argument(
		'-e',
		'--regex',
		nargs=1,
		help='specify regex'
	)
	parse.add_argument(
		'-L',
		'--last',
		action='store_true',
		dest='is_last',
		default=False,
		help='use the last renaming method'
	)
	parse.add_argument(
		'-c',
		'--cat',
		action='store_true',
		dest='is_cat',
		default=False,
		help='show information that the last renaming methods'
	)
	parse.add_argument(
		'-d',
		'--delete',
		nargs=1,
		help='delete words in filename, the argument required: -p/--path'
	)
	parse.add_argument(
		'-n',
		'--normal',
		action='store_true',
		dest='is_normal',
		default=False,
		help='rename normal files'
	)
	args = parse.parse_args()

	# 批量删除文件名中指定字符
	if args.delete and args.path:
		deleteWords(args.path[0], args.delete[0])
	# 把非序列文件重命名成序列文件
	if args.is_normal:
		if args.prefix:
			Rename_normal_files(args.path[0], args.prefix[0], args.suffix[0])
	# 查看上一次重命名的方法信息
	if args.is_cat:
		ar = last()
		for n in ar:
			print(n)
		print('')
		sys.exit()
	# 使用上一次重命名的方法
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