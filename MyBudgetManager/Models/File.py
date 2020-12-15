from sqlalchemy import Column, String, Integer, Date, Boolean
from sqlalchemy.orm import relationship
import os
import datetime
import time
from pathlib import Path

import MyBudgetManager.MyBudgetManager.Models.hash as hash
import MyBudgetManager.MyBudgetManager.Log.logs as logs
from MyBudgetManager.MyBudgetManager.Models.base import Base, Session


class File(Base):

    __tablename__ = 'filecollection'

    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Extension = Column(String)
    CreationDate = Column(Date)
    ModificationDate = Column(Date)
    Path = Column(String)
    Hash = Column(String)
    Status = Column(Boolean)

    def __init__(self, path):
        self.Name = NameOfTheFile(path)
        self.Extension = FileExtension(path)
        self.CreationDate = CreationDate(path)
        self.ModificationDate = ModifiedDate(path)
        self.Path = path
        self.Hash = hash.md5sum(path)
        self.Status = True


path = R"C:\Users\troja\Private\Python\MyBudgetManager\MyBudgetManager\test.py"
extension = "py"


def NameOfTheFile(path):
    """Return the name of the given file.

    Parameters
    ----------
    path : string
        the path of the file

    Returns
    -------
    string
        the name of the file
    """

    logs.logger.debug(
        "Return the name of the given file (%s)." % path)
    try:
        return os.path.basename(path)
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(NameOfTheFile(path))

def CreationDate(path):
    """Return the creation date of the given file

    Parameters
    ----------
    path : string
        the path of the file

    Returns
    -------
    string
        the creation date of the file
    """

    logs.logger.debug(
        "Return the creation date of the given file (%s)." % path)
    try:
        return time.strftime("%Y-%m-%d %I:%M:%S",
                             time.localtime(os.path.getctime(path)))
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(CreationDate(path))

def ModifiedDate(path):
    """Return the modification date of the given file.

    Parameters
    ----------
    path : string
        the path of the file

    Returns
    -------
    string
        the modification date of the file
    """

    logs.logger.debug(
        "Return the modification date of the given file (%s)." % path)
    try:
        return time.strftime("%Y-%m-%d %I:%M:%S",
                             time.localtime(os.path.getmtime(path)))
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(ModifiedDate(path))

def FileExtensionChecker(path, extension):
    """Return TRUE if the given file extension is the same which define in the argument.

    Parameters
    ----------
    path : string
        the path of the file
    extension : string
        the extension type

    Returns
    -------
    boolean
        True if the extension is the same.
    """
    logs.logger.debug(
        "Return TRUE if the given file (%s) extension (%s) is the same which\
             define in the argument." % (path, extension))
    try:
        if path.endswith("." + extension):
            return True
        else:
            return False
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(FileExtensionChecker(path, extension))

def FileExtension(path):
    """Return the extension of the file based on the path.

    Parameters
    ----------
    path : string
        path of the file

    Returns
    -------
    string
        extension type of the file
    """
    logs.logger.debug(
        "Return TRUE if the given file (%s) extension (%s) is the same which\
             define in the argument." % (path, extension))
    try:
        return Path(path).suffix
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(FileExtension(path))
