import MyBudgetManager.MyBudgetManager.Models.hash as hash
import MyBudgetManager.MyBudgetManager.Log.logs as logs
import MyBudgetManager.MyBudgetManager.Models.directory as directory
import MyBudgetManager.MyBudgetManager.Database.FileDBMethods as FileDBMethods

path = R"C:\Users\troja\Private\Python\MyBudgetManager\MyBudgetManager\test.py"
path1 = R"D:\Other"


def IsFileExistsInDB(FilePath):
    """Compare a file's hash to the given hashlist

    Parameters
    ----------
    HashList : list of string
        a list of hashes (in our case from the database)
    FilePath : string
        the path of the given file

    Returns
    -------
    boolean
        True if the file's hash already stored in the database.
    """

    try:
        logs.logger.debug(
            "Compare a file's (%s) hash to the given hashlist" % FilePath)
        HashList = FileDBMethods.GetTheHashListOfFiles()
        result = False
        if hash.md5sum(FilePath) in HashList:
            result = True
        return result
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(IsFileExistsInDB(path))

def CompareDirToDB(DirPath):
    """Compare the files' hashlist of the given directory to the stored hashes
    from the database (or any list of hashes)    

    Parameters
    ----------
    HashList : list of string
        a list of hashes (in our case from the database)
    DirPath : string
        the path of the given directory

    Returns
    -------
    string
        the path of the first new file
    """

    try:
        logs.logger.debug("Compare the files' hashlist of the given directory (%s)\
        to the stored hashes from the database." % DirPath)
        HashListFromDB = FileDBMethods.GetTheHashListOfFiles()
        hashListOfFilesInDirectory = {}
        for filesPath in directory.GetTheFilesPathOfDirectory(DirPath):
            hashListOfFilesInDirectory[filesPath] = hash.md5sum(filesPath)
        return (set(hashListOfFilesInDirectory.values()) == set(HashListFromDB))
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(CompareDirToDB(path1))
