import os, stat, sys, subprocess
from functools import partial
from shutil import rmtree


def findMatches(path, matchName):
	with subprocess.Popen(['cmd', '/c', 'dir', matchName, '/b', '/s', '/a'], stdout=subprocess.PIPE, cwd=path) as dir:
		return dir.communicate()[0].splitlines()


def removeReadOnly(func, path, excInfo):
	os.chmod(path, stat.S_IWRITE)
	os.remove(path)


subdirs = lambda path: [os.path.join(path, d) for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
directoryMatchesName = lambda matchName, path: len(os.path.split(path)) > 1 and os.path.split(path)[1].casefold() == matchName.casefold()


if len(sys.argv) < 2:
	print('Syntax: deleteSubDirs dirName [rootDir] [q]')
	quit()
wantedName = sys.argv[1]

root = '.'
if len(sys.argv) > 2:
	root = sys.argv[2]

quiet = False
if len(sys.argv) > 3:
	quiet = sys.argv[3].casefold == 'q'.casefold

print(f'Based off the DIR command, will NOT process {root}\\{wantedName} because of how it matches filenames and paths.')

deleteList = findMatches(root, wantedName)

print(deleteList)
if quiet or input('Delete these matching dirs? [y/N] ').casefold == 'y'.casefold:
	for d in deleteList:
		try:
			# Deletes entire trees with files
			rmtree(d, onerror=removeReadOnly)
		except Exception as e:
			print(e)

