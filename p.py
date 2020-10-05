#!/usr/bin/python
import filecmp
import os.path
import shutil
from pprint import pprint
print("Comparing directories:")

def compare_dirs(dir1, dir2):
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param dir1: First directory path
    @param dir2: Second directory path

    @return: True if the directory trees are the same and
        there were no errors while accessing the directories or files,
        False otherwise.
   """

    dirs_cmp = filecmp.dircmp(dir1, dir2)
    if len(dirs_cmp.left_only)>0 or len(dirs_cmp.right_only)>0 or \
        len(dirs_cmp.funny_files)>0:
        return False
    (_, mismatch, errors) =  filecmp.cmpfiles(
        dir1, dir2, dirs_cmp.common_files, shallow=False)
    if len(mismatch)>0 or len(errors)>0:
        return False
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not are_dir_trees_equal(new_dir1, new_dir2):
            return False
    return True
print("Enter first directory")
dir1 = raw_input()
print("Enter second directory")
dir2 = raw_input()
if (compare_dirs(dir1, dir2)):
        print("Directories are equal!")
else:
        print("Directories aren't equal!")
        #entries = os.listdir(dir1)
	files_dir1 = os.listdir(dir1)
	files_dir2 = os.listdir(dir2)
	total = len(files_dir1)
	for i in range(total):
		mtime1 = os.path.getmtime(dir1+"/"+files_dir1[i])
		mtime2 = os.path.getmtime(dir2+"/"+files_dir2[i])
		if mtime1 != mtime2:
			if mtime1 < mtime2:
				print(dir1+"/"+files_dir1[i]+" is older than "+dir2+"/"+files_dir2[i])
				print("remove "+dir1+"/"+files_dir1[i])
				os.remove(dir1+"/"+files_dir1[i])
				print("copy "+dir2+"/"+files_dir2[i]+" to "+dir1)
				shutil.copy2(dir2+"/"+files_dir2[i], dir1+"/"+files_dir2[i])
			else:
				print(dir2+"/"+files_dir2[i]+" is older than "+dir1+"/"+files_dir1[i])
                                print("remove "+dir2+"/"+files_dir2[i])
                                os.remove(dir2+"/"+files_dir2[i])
                                print("copy "+dir1+"/"+files_dir1[i]+" to "+dir2)
                                shutil.copy2(dir1+"/"+files_dir1[i], dir2+"/"+files_dir1[i])

		else:
			print(dir1+"/"+files_dir1[i]+" and "+dir2+"/"+files_dir2[i]+" are equals ")
