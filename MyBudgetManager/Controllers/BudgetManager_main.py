import sys
import os
from datetime import date
import xml.etree.ElementTree as ET

import MyBudgetManager.MyBudgetManager.Models.Cost as Cost
import MyBudgetManager.MyBudgetManager.Database.CostMethods as CostMethods
import MyBudgetManager.MyBudgetManager.Models.Income as Income
import MyBudgetManager.MyBudgetManager.Database.IncomeMethods as IncomeMethods
import MyBudgetManager.MyBudgetManager.Database.FileDBMethods as FileDBMethods
import MyBudgetManager.MyBudgetManager.XML_Converter as XML_Converter
import MyBudgetManager.MyBudgetManager.Models.EnumCategory as EnumCategory
import MyBudgetManager.MyBudgetManager.Models.File as File
from MyBudgetManager.MyBudgetManager.Models.base import session


def main():
    ListOfNewFiles = FileDBMethods.NewFilesInDB()
    for NewFile in ListOfNewFiles:
        path = NewFile.Path
        tree = ET.parse(path)
        root = tree.getroot()
        XML_Converter.ParserFromXMLToDataBase(root)
        FileDBMethods.ModifyStatusOfTheFileFromNewToOld(NewFile)

    # newCost = Cost.Cost(date(2021, 3, 31), date(2021, 3, 31),
    #                     10, "Nyuszifarok", "Shopping")
    # CostMethods.AddCost(newCost)

    # CostMethods.DeleteCost(17)

    # CostMethods.ModifyTheFullRowOfCost(27, date(2021, 1, 1), date(
    #     2021, 1, 7), 314, "Phi", "Tinus Lunch")

    # CostMethods.ModifyRegistrationDateOfCost(31, date(2019, 3, 16))

    # CostMethods.ModifyDateOfPaymentOfCost(3, date(2007, 3, 16))

    # CostMethods.ModifyAmountOfCost(4, 125698)

    # CostMethods.ModifyDescriptionOfCost(10, "Juventus mez")

    # CostMethods.ModifyCategoryOfCost(39, "Garbage Delivery")

    # CostMethods.PrintAllCosts()

    # myCost = CostMethods.GetCostByIDFromDB(9)
    # print(myCost.category)

    # CostMethods.GetAllRegistrationDateOfCost()
    # print(CostMethods.GetAllRegistrationDateOfCost())
    # print(type(CostMethods.GetAllRegistrationDateOfCost()))

    # CostMethods.GetAllDateOfPaymentOfCost()
    # print(CostMethods.GetAllDateOfPaymentOfCost())

    # CostMethods.GetAllAmountOfCost()
    # print(CostMethods.GetAllAmountOfCost())
    # print(type(CostMethods.GetAllAmountOfCost()))

    # CostMethods.GetAllDescriptionOfCost()
    # print(CostMethods.GetAllDescriptionOfCost())

    # CostMethods.GetAllCategoryOfCost()
    # print(CostMethods.GetAllCategoryOfCost())

    # CostMethods.GetAllDifferentRegistrationDateOfCost()
    # print(CostMethods.GetAllDifferentRegistrationDateOfCost())

    # CostMethods.GetAllDifferentDateOfPaymentOfCost()
    # print(CostMethods.GetAllDifferentDateOfPaymentOfCost())

    # CostMethods.GetAllDifferentAmountOfCost()
    # print(CostMethods.GetAllDifferentAmountOfCost())

    # CostMethods.GetAllDifferentDescriptionOfCost()
    # print(CostMethods.GetAllDifferentDescriptionOfCost())

    # CostMethods.GetAllDifferentCategoryOfCost()
    # print(CostMethods.GetAllDifferentCategoryOfCost())

    # CostMethods.SumTotalCost()
    # print(CostMethods.SumTotalCost())
    # print(type(CostMethods.SumTotalCost()))

    # print(CostMethods.GetAllCostByRegistrationDateFromDB(date(2019, 2, 13)))
    # print(type(CostMethods.GetAllCostByRegistrationDateFromDB(date(2019, 2, 13))))
    # CostMethods.PrintCosts(
    #     CostMethods.GetAllCostByRegistrationDateFromDB(date(2019, 2, 13)))

    # print(CostMethods.GetAllCostByDateOfPaymentFromDB(date(2021, 3, 16)))
    # print(type(CostMethods.GetAllCostByDateOfPaymentFromDB(date(2021, 3, 16))))
    # CostMethods.PrintCosts(
    #    CostMethods.GetAllCostByDateOfPaymentFromDB(date(2021, 3, 16)))

    # print(CostMethods.GetAllCostByAmountFromDB(1250))
    # print(type(CostMethods.GetAllCostByAmountFromDB(1250)))
    # CostMethods.PrintCosts(
    #    CostMethods.GetAllCostByAmountFromDB(1250))

    # print(CostMethods.GetAllCostByDescriptionFromDB("Új bejegyzés"))
    # print(type(CostMethods.GetAllCostByDescriptionFromDB("Új bejegyzés")))
    # CostMethods.PrintCosts(
    #     CostMethods.GetAllCostByDescriptionFromDB("Új bejegyzés"))

    # print(CostMethods.GetAllCostsFromDB())
    # print(type(CostMethods.GetAllCostsFromDB()))
    # CostMethods.PrintCosts(
    #     CostMethods.GetAllCostsFromDB())

    # print(CostMethods.GetAllCostByCategoryFromDB("Loci Lunch"))
    # print(type(CostMethods.GetAllCostByCategoryFromDB("Loci Lunch")))
    # CostMethods.PrintCosts(
    #    CostMethods.GetAllCostByCategoryFromDB("Loci Lunch"))

    # print(CostMethods.GetAllCostByAmountBandFromDB(1250, 350000))
    # print(type(CostMethods.GetAllCostByAmountBandFromDB(1250, 350000)))
    # CostMethods.PrintCosts(
    #    CostMethods.GetAllCostByAmountBandFromDB(1250, 350000))

    # print(CostMethods.GetAllCostByDateOfPaymentBandFromDB(
    #    date(2019, 2, 12), date(2021, 3, 16)))
    # print(type(CostMethods.GetAllCostByDateOfPaymentBandFromDB(
    #    date(2021, 3, 1), date(2021, 3, 16))))
    # CostMethods.PrintCosts(
    #    CostMethods.GetAllCostByDateOfPaymentBandFromDB(date(2019, 2, 12), date(2021, 3, 16)))

    # print(CostMethods.SumCostByCategory("Shopping"))
    # print(type(CostMethods.SumCostByCategory("Loci Lunch")))

    # print(CostMethods.SumCostByDay(date(2019, 2, 12)))
    # print(type(CostMethods.SumCostByDay(date(2021, 3, 16))))

    # print(CostMethods.SumCostByMonth(2021, 3))
    # print(type(CostMethods.SumCostByMonth(2021, 3)))

    # print(CostMethods.SumCostByQuarter(2021, 1))
    # print(type(CostMethods.SumCostByQuarter(2021, 1)))

    # print(CostMethods.SumCostByYear(2021))
    # print(type(CostMethods.SumCostByYear(2021)))

    # print(CostMethods.SumCostByBetweenDates(
    #     date(2021, 1, 12), date(2021, 3, 31)))
    # print(type(CostMethods.SumCostByBetweenDates(
    #     date(2021, 1, 12), date(2021, 3, 31))))

    # print(CostMethods.SumCostByDayPerCategory(date(2019, 2, 12), "Loci Lunch"))

    # print(CostMethods.SumCostByMonthPerCategory(2021, 3, "Shopping"))

    # print(CostMethods.SumCostByQuarterPerCategory(
    #     2021, 1, "Electricity Service"))

    # print(CostMethods.SumCostByYearPerCategory(
    #     2019, "Shopping"))

    # print(CostMethods.SumCostByBetweenDatesPerCategory(
    #     date(2019, 1, 12), date(2021, 3, 31), "Shopping"))

    # print(CostMethods.SearcherInDescription("cudar draga "))
    # print(type(CostMethods.SearcherInDescription("cudar draga ")))
    # CostMethods.PrintCosts(
    #     CostMethods.SearcherInDescription("cudar draga "))

    # IncomeMethods.PrintAllIncomes()

    # newIncome = Income.Income(date(2021, 3, 31), date(2021, 3, 31),
    #                           10, "új bevétel", "Interest Income and Other Revenue From Bank")
    # IncomeMethods.AddIncomes(newIncome)

    # IncomeMethods.DeleteIncome(1)

    # CostMethods.ModifyTheFullRowOfCost(27, date(2021, 1, 1), date(
    #     2021, 1, 7), 314, "Phi", "Tinus Lunch")

    # IncomeMethods.ModifyTheFullRowOfIncome(2, date(2021, 1, 1), date(
    #     2021, 1, 7), 314, "nu megy ez", "Tinus's Cafeteria")

    # IncomeMethods.ModifyRegistrationDateOfIncome(2, date(1763, 1, 1))

    # IncomeMethods.ModifyDateOfPaymentOfIncome(3, date(1963, 1, 1))

    # IncomeMethods.ModifyAmountOfIncome(3, 56988)

    # IncomeMethods.ModifyDescriptionOfIncome(3, "Nu ezt is siokerült")

    # IncomeMethods.ModifyCategoryOfIncome(
    #     2, "Interest Income and Other Revenue From Bank")

    # myCost = CostMethods.GetCostByIDFromDB(9)
    # print(myCost.category)

    # myIncome = IncomeMethods.GetIncomeByIDFromDB(2)
    # print(myIncome.category.value)

    # print(CostMethods.GetAllCostByRegistrationDateFromDB(date(2019, 2, 13)))
    # print(type(CostMethods.GetAllCostByRegistrationDateFromDB(date(2019, 2, 13))))
    # CostMethods.PrintCosts(
    #     CostMethods.GetAllCostByRegistrationDateFromDB(date(2019, 2, 13)))

    # print(IncomeMethods.GetAllIncomeByRegistrationDateFromDB(date(1763, 1, 1)))
    # IncomeMethods.PrintIncomes(
    #     IncomeMethods.GetAllIncomeByRegistrationDateFromDB(date(1763, 1, 1)))

    # IncomeMethods.PrintIncomes(
    #     IncomeMethods.GetAllIncomeByDateOfPaymentFromDB(date(1963, 1, 1)))

    # IncomeMethods.PrintIncomes(IncomeMethods.GetAllIncomeByAmountFromDB(314))

    # IncomeMethods.PrintIncomes(
    #     IncomeMethods.GetAllIncomeByDescriptionFromDB("Nu ezt is siokerült"))

    # IncomeMethods.PrintIncomes(IncomeMethods.GetAllIncomeByCategoryFromDB(
    #     "Interest Income and Other Revenue From Bank"))

    # IncomeMethods.PrintIncomes(
    #     IncomeMethods.GetAllIncomeByAmountBandFromDB(2, 70000))

    # IncomeMethods.PrintIncomes(IncomeMethods.GetAllIncomeByDateOfPaymentBandFromDB(
    #     date(1763, 1, 1), date(1964, 1, 1)))

    # print(IncomeMethods.GetAllRegistrationDateOfIncome())

    # print(IncomeMethods.GetAllDateOfPaymentOfIncome())

    # print(IncomeMethods.GetAllAmountOfIncome())

    # print(IncomeMethods.GetAllDescriptionOfIncome())

    # print(IncomeMethods.GetAllCategoryOfIncome())

    # print(IncomeMethods.GetAllDifferentRegistrationDateOfIncome())

    # print(IncomeMethods.GetAllDifferentDateOfPaymentOfIncome())

    # print(IncomeMethods.GetAllDifferentAmountOfIncome())

    # print(IncomeMethods.GetAllDifferentDescriptionOfIncome())

    # print(IncomeMethods.GetAllDifferentCategoryOfIncome())

    # print(IncomeMethods.GetAllIncomesFromDB())

    # print(IncomeMethods.SumTotalIncome())

    # print(IncomeMethods.SumIncomeByCategory("Lóci's salary"))


if __name__ == '__main__':
    sys.exit(main())
