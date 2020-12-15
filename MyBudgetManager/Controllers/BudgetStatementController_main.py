import sys
import os
from datetime import date

import MyBudgetManager.MyBudgetManager.Models.Cost as Cost
import MyBudgetManager.MyBudgetManager.Database.CostMethods as CostMethods
import MyBudgetManager.MyBudgetManager.Models.Income as Income
import MyBudgetManager.MyBudgetManager.Database.IncomeMethods as IncomeMethods
from MyBudgetManager.MyBudgetManager.Models.base import session
import MyBudgetManager.MyBudgetManager.Models.directory as directory
import MyBudgetManager.MyBudgetManager.Database.directoryDBMethods as directoryDBMethods
import MyBudgetManager.MyBudgetManager.Database.FileDBMethods as FileDBMethods
import MyBudgetManager.MyBudgetManager.Models.File as File


# The path where financial statements and
# other evidence can be found in XML format.
path_statement_directory = os.path.abspath(
    "MyBudgetManager/MyBudgetManager/FinancialStatementDirectory")
# StatementPath = R"D:\Python\MyBudgetManager\MyBudgetManager\FinancialStatementDirectory"
extension = "xml"


def main():
    XMLFilesListInFinancialStatementDirectory = directory.GetTheXMLFilesPathOfDirectory(
        path_statement_directory)
    for XMLFile in XMLFilesListInFinancialStatementDirectory:
        if not directoryDBMethods.IsFileExistsInDB(XMLFile):
            FileDBMethods.InsertNewFiles(XMLFile)


if __name__ == '__main__':
    sys.exit(main())
