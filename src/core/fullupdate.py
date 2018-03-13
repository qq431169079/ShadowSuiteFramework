#		 Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

# Python modules

import requests
import json
import os
from packaging import version
import urllib.request
from glob import glob
import shutil
import sys
import distutils.dir_util

def check_for_updates():
	try:
		print(colors.green+"checking for updates..."+colors.end)
		r = requests.get("https://api.github.com/repos/Sh4d0w-T34m/ShadowSuiteLE/releases/latest")
		if(r.ok):
			items = json.loads(r.text or r.content)
			rver = items['tag_name']

			# DEV0003
		else:
			print("error")
	except Exception as error:
		print(colors.red+"error: "+str(error)+colors.end)

def update():
	answer = input("do you want to start update? ")

	if answer != "yes" and answer != "y":
		return


	url = "https://github.com/4shadoww/hakkuframework/tarball/master"
	print(colors.green+"downloading..."+colors.end)

	u = urllib.request.urlopen(url)

	print(colors.green+"clearing tmp..."+colors.end)
	mscop.clear_tmp()

	print(colors.green+"writing..."+colors.end)

	f = open(getpath.tmp()+"update.tar.gz", "wb")
	f.write(u.read())
	f.close()

	print(colors.green+"extracting..."+colors.end)
	os.system("tar -zxvf '"+getpath.tmp()+"update.tar.gz' -C '"+getpath.tmp()+"'")

	files = glob(getpath.tmp()+"*/")
	update_path = None

	for file in files:
		if "hakku" in file and os.path.isfile(file) == False:
			update_path = file
			break

	if update_path == None:
		print(colors.red+"error: update package not found!"+colors.end)
		return

	files = glob(update_path+"*")

	print(colors.green+"installing update..."+colors.end)

	for file in files:

		file_name = file.replace(update_path, "")
		print(getpath.main()+file_name)

		if os.path.isfile(file):
			shutil.copyfile(file, getpath.main()+file_name)
		else:
			distutils.dir_util.copy_tree(file, getpath.main()+file_name)


	print(colors.green+"clearing tmp..."+colors.end)
	mscop.clear_tmp()

	print(colors.green+"update installed! closing Hakku Framework"+colors.end)
	sys.exit()
