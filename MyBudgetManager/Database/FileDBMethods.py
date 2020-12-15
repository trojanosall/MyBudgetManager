import sqlalchemy as sqla

import MyBudgetManager.MyBudgetManager.Log.logs as logs
import MyBudgetManager.MyBudgetManager.Models.File as File
from MyBudgetManager.MyBudgetManager.Models.base import session

path = R"C:\Users\troja\Private\Python\MyBudgetManager\MyBudgetManager\FinancialStatementDirectory\convertcsv.xml"


def GetTheHashListOfFiles():
    """Get the hash list of the files from DB.

    Returns
    -------
    list
        Hash list of the files from DB.
    """

    logs.logger.debug("Get the hash list of the files from DB.")
    try:
        Files = session.query(File.File).all()
        return [File.Hash for File in Files]
    except Exception as e:
        logs.logger.error(e, exc_info=True)

# print(type(GetTheHashListOfFiles()))


def NewFilesInDB():
    """Get the list of new files from DB.

    Returns
    -------
    list
        List of new files from DB.
    """

    logs.logger.debug("Get the list of new files from DB.")
    try:
        ListOfNewFiles = []
        ListOfNewFiles = session.query(File.File).filter(
            File.File.Status == 1).all()
        return ListOfNewFiles
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def InsertNewFiles(path):
    """Insert new file to the database

    Parameters
    ----------
    session : session
        Manages persistence operations for ORM-mapped objects.

    path : string
        the path of the file

    """

    logs.logger.debug("Start insert new file (%s) to the database" % path)
    try:
        newFile = File.File(path)
        session.add(newFile)
        session.commit()
        logs.logger.info("Insert new file (%s) to the database" % path)
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# InsertNewFiles(path)


def GetTheLastFile():
    """Get the last file from the database.

    Parameters
    ----------
    session : session
        Manages persistence operations for ORM-mapped objects.

   path : string
        the path of the file

    Returns
    -------
    ORM-mapped object
        trigger file
    """

    logs.logger.debug("Get the last file from the database.")
    try:
        LastFile = session.query(File.File).order_by('ModificationDate')[-1]
        return LastFile
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(GetTheLastFile())


def PrintFiles(FilesList):
    """Print all files based on the given file list parameter.

    Parameters
    ----------
    FileList : list
        List of Files

    """

    logs.logger.debug(
        "Start to print all files based on the given file list parameter.")
    try:
        for file in FilesList:
            print(
                f'{file.ID}\t{file.Name}\t{file.CreationDate} \
                    \t{file.ModificationDate}\t{file.Path}\t{file.Hash}')
        logs.logger.info(
            "Print all file based on the given costs list parameter.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)

# FileList = session.query(File.File).all()

# PrintFiles(FileList)


# PrintFiles(NewFilesInDB())

def ModifyStatusOfTheFileFromNewToOld(File):
    """Modify the status (new = 1, old = 0) of the file from new to old in DB.

    Parameters
    ----------
    File : object
        File object

    Returns
    -------
    File
        File object
    """
    logs.logger.debug(
        "Modify the status (new = 1, old = 0) of the file from new to old in\
             DB.")
    try:
        File.Status = 0
        session.commit()
        return File
    except Exception as e:
        logs.logger.error(e, exc_info=True)
