import xml.etree.ElementTree as ET
import sys
import os
from datetime import datetime

import MyBudgetManager.MyBudgetManager.Models.Cost as Cost
import MyBudgetManager.MyBudgetManager.Database.CostMethods as CostMethods
import MyBudgetManager.MyBudgetManager.Models.Income as Income
import MyBudgetManager.MyBudgetManager.Database.IncomeMethods as IncomeMethods
from MyBudgetManager.MyBudgetManager.Models.base import session
import MyBudgetManager.MyBudgetManager.Models.EnumCategory as EnumCategory
import MyBudgetManager.MyBudgetManager.Log.logs as logs

path = R"C:\Users\troja\Private\Python\MyBudgetManager\MyBudgetManager\FinancialStatementDirectory\convertcsv.xml"
tree = ET.parse(path)
root = tree.getroot()

magigWordListForTVCostCat = ["DIGI ", "UPC "]
magigWordListForGasCostCat = ["NKM FOLDGAZSZOLGALTATO "]
magigWordListForElectricityCostCat = ["ELMU-EMASZ "]
magigWordListForWaterCostCat = ["VIZ "]
magigWordListForHeatingCostCat = ["FOTAV "]
magigWordListForGarbageCostCat = ["NHKV "]
magigWordListForLoanCostCat = [
    "TOKE ", "KAMAT ", "JJ5CF00020877", "JJ4CF00020865"]
magigWordListForGiftCostCat = ["AJANDEK "]
magigWordListForShoppingCostCat = [
    "SPAR ", "PEPCO ", "ALDI ", "AUCHAN ", "ABC ", "TESCO ", "KIK ", "DM ",
    "PENNY ", "ELEMISZERB", "IKEA ", "LIPOTI ", "LIBRI ", "LIDL ",
    "CALZEDONIA "]
magigWordListForElectronicCostCat = ["EMAG  ", "MEDIA MARKT "]
magigWordListForLiliCostCat = ["MARIA MONTESSORI "]
magigWordListForBankCostCat = ["JUTALEK ", "SZAMLAVEZETESI DIJ "]
magigWordListForTinusLunchCostCat = ["ATRIUM ", "ETTER ", "HAI NAM "]
magigWordListForLociLunchCostCat = ["ATRIUM ", "ETTER ", "HAI NAM "]
magigWordListForTrafficCostCat = [
    "KELEN ", "JEGYKIA ", "BKK AUTOMATA ", "BKK "]
magigWordListForTobaccoCostCat = ["NEMZETI DOHA "]
magigWordListForEntertainmentCostCat = ["CAFE ", "FREI ", "CINEMA ", "CAFFE "]
magigWordListForTinusMobileCostCat = ["VODAFONE "]
magigWordListForCommonCostCat = ["KOZOS ", "TEMPLOM "]
magigWordListForRentingRelatedCostCat = ["FOTAV ", "TEMPLOM "]
magigWordListForPetrolCostCat = ["BENZ-OIL ",
                                 "OIL ", "MOL ", "SHELL ", "OMV ", "LUKOIL "]
magigWordListForHealthCostCat = [
    "ARANYCSILLAG ", "GYOGYSZER ", "GYSZERTA", "EGESZSEG"]
magigWordListForLociSalaryIncCat = [
    "EVOSOFT ", "KEDVEZMENYEZETT NEVE: LAJOS LORANT ", "BER ", "FIZETES ",
    "MUNKABER "]
magigWordListForTinusSalaryIncCat = [
    "NN BIZTOSITO ", "KEDVEZMENYEZETT NEVE: LAJOS-KOVACS ", "BER ", "FIZETES ",
    "MUNKABER "]
magigWordListForLociCafeteriaIncCat = ["CAFETERIA"]
magigWordListForTinusCafeteriaIncCat = ["CAFETERIA"]
magigWordListForBankRevenueIncCat = ["DIJKEDVEZMENY", "KAMAT"]

EnumCatVSMagicWordDict = {
    EnumCategory.EnumCategory.catTvAndInternet: magigWordListForTVCostCat,
    EnumCategory.EnumCategory.catGasService: magigWordListForGasCostCat,
    EnumCategory.EnumCategory.catElectricityService:
    magigWordListForElectricityCostCat,
    EnumCategory.EnumCategory.catWaterSupply: magigWordListForWaterCostCat,
    EnumCategory.EnumCategory.catHeatingService:
    magigWordListForHeatingCostCat,
    EnumCategory.EnumCategory.catGarbageDelivery:
    magigWordListForGarbageCostCat,
    EnumCategory.EnumCategory.catLoanRepayment: magigWordListForLoanCostCat,
    EnumCategory.EnumCategory.catGift: magigWordListForGiftCostCat,
    EnumCategory.EnumCategory.catShopping: magigWordListForShoppingCostCat,
    EnumCategory.EnumCategory.catElectronicGoods:
    magigWordListForElectronicCostCat,
    EnumCategory.EnumCategory.catLili: magigWordListForLiliCostCat,
    EnumCategory.EnumCategory.catBankCharges: magigWordListForBankCostCat,
    EnumCategory.EnumCategory.catTinusLunch: magigWordListForTinusLunchCostCat,
    EnumCategory.EnumCategory.catLociLunch: magigWordListForLociLunchCostCat,
    EnumCategory.EnumCategory.catTraffic: magigWordListForTrafficCostCat,
    EnumCategory.EnumCategory.catTobacco: magigWordListForTobaccoCostCat,
    EnumCategory.EnumCategory.catEntertainment:
    magigWordListForEntertainmentCostCat,
    EnumCategory.EnumCategory.catTinusMobile:
    magigWordListForTinusMobileCostCat,
    EnumCategory.EnumCategory.catCommonCost: magigWordListForCommonCostCat,
    EnumCategory.EnumCategory.catRentingRelatedCost:
    magigWordListForRentingRelatedCostCat,
    EnumCategory.EnumCategory.catPetrol: magigWordListForPetrolCostCat,
    EnumCategory.EnumCategory.catHealth: magigWordListForHealthCostCat,
    EnumCategory.EnumCategory.catLociSalary: magigWordListForLociSalaryIncCat,
    EnumCategory.EnumCategory.catTinusSalary:
    magigWordListForTinusSalaryIncCat,
    EnumCategory.EnumCategory.catLociCafeteria:
    magigWordListForLociCafeteriaIncCat,
    EnumCategory.EnumCategory.catTinusCafeteria:
    magigWordListForTinusCafeteriaIncCat,
    EnumCategory.EnumCategory.catBankIncomeAndOther:
    magigWordListForBankRevenueIncCat
}

# x = EnumCatVSMagicWordDict.get(EnumCategory.EnumCategory.catShopping)

# print(x)

# for item in EnumCatVSMagicWordDict:
#     print(item)

# for item in EnumCatVSMagicWordDict:
#     print(EnumCatVSMagicWordDict[item])

# test_text = "Kimeno eseti utalas   SPETES0099257593 16300000-04009163-90106414 Magyarorszag VODAFONE Kozlemeny: 34396433 - Fiz.hat.: 02/04, Lajos-Kovacs Krisztina Erteknap: 2019.02.04"


# for keyItem in EnumCatVSMagicWordDict:
#     category = ""
#     for value in EnumCatVSMagicWordDict.get(keyItem):
#         if value in test_text.upper():
#             category = keyItem.value
#             print(keyItem.value)
# if category is "":
#     print("Sorryy.....")


def CategoryFinderBasedOnDescription(description):
    """Based on description of Cost/Income object find the enum category

    Parameters
    ----------
    description : string
        Description of the Cost/Income object.

    Returns
    -------
    Enum
        enum category
    """
    logs.logger.debug(
        "Based on description (%s) of Cost/Income object find the enum category." % description)
    try:
        category = EnumCategory.EnumCategory.catNPerA.value
        for keyItem in EnumCatVSMagicWordDict:
            for value in EnumCatVSMagicWordDict.get(keyItem):
                if value in description.upper():
                    category = keyItem.value
                    break
            else:
                continue
            break
        logs.logger.info(
            "Based on description (%s) of Cost/Income object find the enum category." % description)
        return category
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# print(CategoryFinderBasedOnDescription(test_text))


def PrintTheWholeXMLFile(root):
    """Print the whole XML file.

    Parameters
    ----------
    root : XML parser root
        XML parser root
    """
    logs.logger.debug(
        "Print the whole XML file.")
    try:
        for row in root.findall("row"):
            dateOfPayment = row.find("Konyvelesidatum").text
            description = row.find("Leiras").text
            amount = row.find("Osszeg").text
            print(dateOfPayment, description, amount)
            print()
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# PrintTheWholeXMLFile(root)


def convertDateOfXMLFile(root):
    """Convert date of the XML file.

    Parameters
    ----------
    root : XML parser root
        XML parser root
    """
    logs.logger.debug("Start to convert date of the XML file.")
    try:
        for row in root.findall("row"):
            dateOfPayment = row.find("Konyvelesidatum").text
            convertedDateOfPayment = datetime.strptime(
                dateOfPayment, "%m/%d/%Y").date()
            print(convertedDateOfPayment)
        logs.logger.info("Convert date of the XML file.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# convertDateOfXMLFile()

def ParserFromXMLToDataBase(root):
    """Parsing the Cost/Income object from XML file to DB.

    Parameters
    ----------
    root : XML parser root
        XML parser root
    """
    logs.logger.debug(
        "Start to parse the Cost/Income object from XML file to DB.")
    try:
        for row in root.findall("row"):
            registrationDate = datetime.today()
            dateOfPayment = row.find("Konyvelesidatum").text
            convertedDateOfPayment = datetime.strptime(
                dateOfPayment, "%m/%d/%Y").date()
            description = row.find("Leiras").text
            amount = int(
                float((row.find("Osszeg").text).replace(
                    ",", ".").replace(" ", "")))
            category = CategoryFinderBasedOnDescription(description)
            if amount < 0:
                newCost = Cost.Cost(
                    registrationDate,
                    convertedDateOfPayment, -amount, description, category)
                CostMethods.AddCost(newCost)
            else:
                newIncome = Income.Income(
                    registrationDate,
                    convertedDateOfPayment, amount, description, category)
                IncomeMethods.AddIncomes(newIncome)
        logs.logger.info("Parsing the Cost/Income object from XML file to DB.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


# ParserFromXMLToDataBase(root)
# print("Hehe")
