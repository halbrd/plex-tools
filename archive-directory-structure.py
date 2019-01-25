import os
import datetime

def list_files(startpath):
	out = ""
	for root, dirs, files in os.walk(startpath):
		level = root.replace(startpath, '').count(os.sep)
		indent = ' ' * 1 * (level)
		out += '{}{}/'.format(indent, os.path.basename(root)) + "\n"
		subindent = ' ' * 1 * (level + 1)
		for f in files:
			if f != os.path.basename(__file__):
				out += '{}{}'.format(subindent, f) + "\n"
	return out

with open(os.path.basename(os.path.dirname(__file__)) + datetime.datetime.now().strftime(" %Y-%m-%d %H-%M-%S.txt"), "w") as f:
	f.write(list_files("."))