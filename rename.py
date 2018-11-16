#! python3
# rename.py

import shutil, os, re, sys
import logging

regexText = ['\D?(\d{1,2})', '.*[eE](\d{1,2})']

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
log = logging.getLogger(__name__)

def init(args):
	arguments = []
	if args.path and os.path.exists(args.path[0]):
		os.chdir(args.path[0])
		arguments.append(os.path.abspath(args.path[0]))
	else:
		log.error('the following arguments are required: path, or the path no exists.')
		log.info('<mr -h> get help')
		sys.exit()

	if args.prefix and args.suffix:
		arguments.append(args.prefix[0])
		arguments.append(args.suffix[0])
	else:
		log.error('the following arguments are required: -pre and -suf')
		sys.exit()
	if args.is_one:
		arguments.append(regexText[0])
	elif args.is_two:
		arguments.append(regexText[1])
	elif args.regex:
		arguments.append(args.regex[0])
	else:
		log.error('the following arguments are required: -1, -2 or -3')
		sys.exit()
	os.makedirs('D:/Tools/mr_caches', exist_ok=True)
	f = open('D:/Tools/mr_caches/.rename.bak', 'a+')
	for ar in arguments:
		f.write(ar + '\n')

	return arguments

def last():
	if not os.path.exists('D:/Tools/mr_caches/.rename.bak'):
		log.error('no found .rename.bak file.')
		sys.exit()
	f = open('D:/Tools/mr_caches/.rename.bak', 'r')
	if not f:
		log.info('backup is none')
		sys.exit()
	arguments = f.readlines()
	i = 0
	for i in range(1, len(arguments)+1):
		arguments[-i] = arguments[-i][0:-1]		# 去除末尾'\n'
		i = i + 1
	if not os.path.exists(arguments[-4]):
		log.error('[{}] no exists.'.format(arguments[-4]))
		sys.exit()
	os.chdir(arguments[-4])
	return arguments

def show_rename_files():
	"""显示要重命名的文件"""
	ext = ['.mp4', 'mkv', '.avi', '.wmv', '.pdf']
	filenames = []
	log.info('下列文件即将被重命名：')
	for filename in os.listdir('.'):
		if os.path.splitext(filename)[1] in ext:
			filenames.append(filename)
			log.info(filename)
	return filenames


def Rename(filenames, prefix, suffix, text):
	"""按照序数一一对应重命名"""

	regexNum = re.compile(text)
	newNames = {}
	print('')
	log.info('重命名预览:')
	for filename in filenames:
		mo = regexNum.search(filename)
		if mo:
			newName = ''
			i = int(mo.group(1))
			if i < 10:
				num = '0' + str(i)
			else:
				num = str(i)
			temp = filename.lower()
			if temp.endswith('.mp4'):
				newName += prefix + num + suffix + '.mp4'
			elif temp.endswith('.mkv'):
				newName += prefix + num + suffix + '.mkv'
			elif temp.endswith('.avi'):
				newName += prefix + num + suffix + '.avi'
			elif temp.endswith('.wmv'):
				newName += prefix + num + suffix + '.wmv'
			elif temp.endswith('.pdf'):
				newName += prefix + num + suffix + '.pdf'

			if newName != filename and newName != '':
				log.info(filename + ' to ' + newName)
				newNames[filename] = newName

	if not newNames:
		log.info('新旧文件名相同，无需命名')
		sys.exit()

	flag = input('\n是否重命名(y|n): ')
	if flag == 'y':
		print('')
		log.info('开始重命名...')
		for filename, newName in newNames.items():
			log.info(filename + ' to ' + newName)
			shutil.move(filename, newName)
		log.info('Done!')
	else:
		sys.exit()

def deleteWords(path, text):
	deleteRegex = re.compile(text)
	os.chdir(path)
	newNames = {}
	log.info('重命名预览:')
	for filename in os.listdir('.'):
		mo = deleteRegex.search(filename)
		if mo:
			newName = deleteRegex.sub('', filename)
			if newName != filename and newName != '':
				log.info(filename + ' to ' + newName)
				newNames[filename] = newName
	
	if not newNames:
		log.info('新旧文件名相同，无需命名， 或者文件名中不存在[{}]'.format(text))
		sys.exit()

	flag = input('\n是否重命名(y|n): ')
	if flag == 'y':
		print('')
		log.info('开始重命名...')
		for filename, newName in newNames.items():
			log.info(filename + ' to ' + newName)
			shutil.move(filename, newName)
		log.info('Done!')
		sys.exit()
	else:
		sys.exit()