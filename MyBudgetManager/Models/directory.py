import os
import shutil
import platform
from datetime import datetime, timedelta

import MyBudgetManager.MyBudgetManager.Models.hash as hash
import MyBudgetManager.MyBudgetManager.Log.logs as logs
from MyBudgetManager.MyBudgetManager.Models.base import session
import MyBudgetManager.MyBudgetManager.Models.File as File

# path = R"C:\Users\troja\Private\Python\MyBudgetManager\MyBudgetManager"
# path_dir = R"C:\Users\troja\Private\Python\MyBudgetManager\MyBudgetManager"
# otherPath = R"D:\Other"
# paths_List = [path_dir, otherPath]
path = R"C:\Users\troja\Private\Python\MyBudgetManager\MyBudgetManager\FinancialStatementDirectory"


def GetTheFilesPathOfDirectory(pathOfDir):
    """Create a list of the files' pathes in the given directory.

    Parameters
    ----------
    pathOfDir : string
        the path of a given directory

    Returns
    -------
    list of string
        returns the list of the paths of the files of the given directory
    """

    try:
        logs.logger.debug(
            "Create a list of the files' pathes in the given directory\
                 ( %s )." % pathOfDir)
        listOfFiles = list()
        for (dirpath, dirnames, filenames) in os.walk(pathOfDir):
            listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        return listOfFiles
    except Exception as e:
        logs.logger.error(e, exc_info=True)

# print(GetTheFilesPathOfDirectory(path))


def GetTheXMLFilesPathOfDirectory(pathOfDir):
    """Create a list of the XML files' pathes in the given directory.

    Parameters
    ----------
    pathOfDir : string
        the path of a given directory

    Returns
    -------
    list of string
        returns the list of the paths of the files of the given directory
    """
    try:
        logs.logger.debug(
            "Create a list of the XML files' pathes in the given directory\
                 ( %s )." % pathOfDir)
        listOfFiles = GetTheFilesPathOfDirectory(pathOfDir)
        XMLFilesListInFinancialStatementDirectory = []
        for file in listOfFiles:
            if File.FileExtensionChecker(file, "xml"):
                XMLFilesListInFinancialStatementDirectory.append(file)
        return XMLFilesListInFinancialStatementDirectory
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(GetTheXMLFilesPathOfDirectory(path))


def CreateHashDict(pathOfDir):
    """Create a dictionary from the files' paths and their hashes in the given
    directory

    Parameters
    ----------
    pathOfDir : string
        [description]

    Returns
    -------
    Dictionary
        filepath-hash pairs of the given directory
    """

    try:
        logs.logger.debug("Create a dictionary from the files' paths and their\
            hashes in the given directory")
        hashList = {}
        for filesPath in GetTheFilesPathOfDirectory(pathOfDir):
            hashList[filesPath] = hash.md5sum(filesPath)
        return hashList
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(CreateHashDict(path))

def CreateHashDictForXMLFiles(pathOfDir):
    """Create a dictionary from the xml files' paths and their hashes in the given
    directory

    Parameters
    ----------
    pathOfDir : string
        [description]

    Returns
    -------
    Dictionary
        filepath-hash pairs of the given directory
    """

    try:
        logs.logger.debug("Create a dictionary from the xml files' paths and their\
            hashes in the given directory")
        hashList = {}
        for filesPath in GetTheXMLFilesPathOfDirectory(pathOfDir):
            hashList[filesPath] = hash.md5sum(filesPath)
        return hashList
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(CreateHashDictForXMLFiles(path))


def CompareDirToDir(DirPath1, DirPath2):
    """Compare the contents of two directory with hashes

    Parameters
    ----------
    DirPath1 : string
        the path of the given directory
    DirPath2 : string
        the path of the given directory

    Returns
    -------
    boolean
        True if the two directory are the same
    """

    try:
        logs.logger.debug("Compare the contents of two directory with hashes.")
        hashList1 = {}
        for filesPath in GetTheFilesPathOfDirectory(DirPath1):
            hashList1[filesPath] = hash.md5sum(filesPath)
        hashList2 = {}
        for filesPath in GetTheFilesPathOfDirectory(DirPath2):
            hashList2[filesPath] = hash.md5sum(filesPath)
        return set(hashList1.values()) == set(hashList2.values())
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(CompareDirToDir(path, path))


def CopyDirectory(srcdir, dstdir, symlinks=False, ignore=None):
    """Copy the content of the given directory to another directory

    Parameters
    ----------
    srcdir : string
        the path of the source directory
    dstdir : string
        the path of the destination directory
    symlinks : bool, optional
        [description] (the default is False, which [default_description])
    ignore : [type], optional
        [description] (the default is None, which [default_description])
    """

    try:
        logs.logger.debug(
            "Start copy the content of the %s to %s" % (srcdir, dstdir))
        if not os.path.exists(dstdir):
            os.makedirs(dstdir)
            shutil.copystat(srcdir, dstdir)
        lst = os.listdir(srcdir)
        for item in lst:
            s = os.path.join(srcdir, item)
            d = os.path.join(dstdir, item)
            if symlinks and os.path.islink(s):
                if os.path.lexists(d):
                    os.remove(d)
                    os.symlink(os.readlink(s), d)
            elif os.path.isdir(s):
                CopyDirectory(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)
        logs.logger.info("Copy one directory content to %s" % dstdir)
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# CopyDirectory(path, otherPath)

def DeleteTheDirContent(dirpath):
    """Delete a directory's content

    Parameters
    ----------
    dirpath : string
        the path of the directory
    """
    try:
        logs.logger.debug("Delete  %s's content" % dirpath)
        for root, dirs, files in os.walk(dirpath):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# DeleteTheDirContent(otherPath)

def CreateDirectory(ASPath, yourRootDirectory):
    """Create a directory which name is the label of the Account Statement.

    Parameters
    ----------
    ASPath : string
        the path of the Account Statement file
    yourRootDirectory : string
        the path of the basic directory on the server PC where you want to
        copy the Account Statement file
    """

    try:
        logs.logger.debug(
            "Create a directory which name is the label of the Account\
                 Statement.")
        filename = os.path.basename(path)
        label = filename.split(".")[0]
        logs.logger.debug("Start create the %s directory" % label)
        os.makedirs(yourRootDirectory +
                    "\\" + label, exist_ok=False)
        logs.logger.info("Create the %s directory" % label)
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# CreateDirectory(path, otherPath)

def IsDirExists(path):
    """Check the given directory's existence

    Parameters
    ----------
    path : string
        the path of the directory

    Returns
    -------
    boolean
        True if the directory exists
    """

    try:
        exist = os.path.exists(path)
        logs.logger.debug("The %s is exist: %s" % (path, exist))
        return exist
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(IsDirExists(otherPath))


def AreAllDirExist(paths):
    """Check the given directories' existence

    Parameters
    ----------
    paths : list of string
        the paths of the directories

    Returns
    -------
    boolean
        True if all the directories exist
    """

    try:
        exist = True
        for path in paths:
            if IsDirExists(path) is False:
                exist = False
                break
        logs.logger.info("All drives are exist: %s" % exist)
        return exist
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(AreAllDirExist(paths_List))
