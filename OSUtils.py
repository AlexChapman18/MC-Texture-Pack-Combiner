import os.path
from os import walk
from shutil import copytree
import shutil


def getFiles(path):
    return next(walk(path), (None, None, []))[2]


def getFolders(path):
    return next(walk(path), (None, [], None))[1]


def copyFolder(src, dst):
    copytree(src, dst, dirs_exist_ok=True)


def copyFile(src, dst):
    shutil.copy(src, dst)


def exists(path):
    return os.path.exists(path)


def copyFileNewName(src, dst):
    shutil.copyfile(src, dst)
