# This file just does a `git status` on all the
# folders in the main git folder.
# It'll tell you which ones need to have things commited


import os
import git

rootdir = '../'
dirList = os.listdir(rootdir)
# print dirList

dirsToCommit = []
dirsToGit = []
dirsToCheck = []

for thisDir in dirList:
    try:
        s = git.cmd.Git(rootdir+thisDir).status()
        if "Changes not staged for commit" in s:
            print thisDir
            print s, "\n"
            dirsToCheck.append(thisDir)
        else:
            print thisDir, "good to go"
    except:
        print "***", thisDir, "isn't a git repo"
        dirsToGit.append(thisDir)

print "\ndirsToCommit:\n", dirsToCommit
print "\ndirsToGit:\n",   dirsToGit
