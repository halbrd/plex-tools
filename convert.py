import os
import subprocess

for file in os.listdir(os.getcwd()):
	if not file.endswith(".py"):
		subprocess.call(["ffmpeg", "-n", "-i", file, "REENCODED-" + file])
