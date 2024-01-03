from os import walk


def getFiles(path):
    return next(walk(path), (None, None, []))[2]


def getFolders(path):
    return next(walk(path), (None, [], None))[1]
