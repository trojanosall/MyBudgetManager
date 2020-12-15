import sqlalchemy as sqla
import datetime
import calendar
from datetime import date
import unicodedata

import MyBudgetManager.MyBudgetManager.Models.Income as Income
from MyBudgetManager.MyBudgetManager.Models.base import session
import MyBudgetManager.MyBudgetManager.Log.logs as logs


def PrintAllIncomes():
    """After queries of all incomes from database this method print the details
    (id, reg.date, date of payment, amount, description, category)
    of the incomes to the consol.

    """

    logs.logger.debug("After queries of all incomes from database start to print"
                      " the details (id, reg.date, date of payment, amount,"
                      " description, category) of the incomes to the consol.")
    try:
        printedIncomes = session.query(Income.Income).all()
        for income in printedIncomes:
            print(
                f'{income.id}\t{income.registrationDate}\t{income.dateOfPayment} \
                    \t{income.amount}\t{income.description}\t{income.category.value}')
        logs.logger.info("After queries of all incomes from database print"
                         " the details (id, reg.date, date of payment, amount,"
                         " description, category) of the incomes to the consol.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def PrintIncomes(IncomeList):
    """Print all incomes based on the given incomes list parameter.

    Parameters
    ----------
    IncomeList : list
        List of Incomes

    """

    logs.logger.debug(
        "Start to print all incomes based on the given incomes list parameter.")
    try:
        for income in IncomeList:
            print(
                f'{income.id}\t{income.registrationDate}\t{income.dateOfPayment} \
                    \t{income.amount}\t{income.description}\t{income.category.value}')
        logs.logger.info(
            "Print all incomes based on the given incomes list parameter.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def AddIncomes(Income):
    """Add Income object to the database.

    Parameters
    ----------
    Income : object
        Income object.

    """

    logs.logger.debug("Start to add Income object to the database.")
    try:
        session.add(Income)
        session.commit()
        logs.logger.info("Add Income object to the database.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def DeleteIncome(idOfIncome):
    """Based on Id parameter of the Income object this method deletes the Income
    object from database.

    Parameters
    ----------
    idOfIncome : integer
        Id of the Income object.

    """

    logs.logger.debug(
        "Start to deletes the Income object from database "
        "based on Id parameter (%s)." % idOfIncome)
    try:
        deletedIncome = session.query(Income.Income).filter(
            Income.Income.id == idOfIncome).one()
        session.delete(deletedIncome)
        session.commit()
        logs.logger.info("Deletes the Income object from database "
                         "based on Id parameter (%s)." % idOfIncome)
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def ModifyTheFullRowOfIncome(idOfIncome, registrationDate, dateOfPayment, amount, description, category):
    """Based on the all given properties of Income as parameters this method
    modifys the properties of Income object in database.

    Parameters
    ----------
    idOfIncome : integer
        Id of Income object.
    registrationDate : date
        Registration date of Income object.
    dateOfPayment : date
        Payment date of Income object.
    amount : integer
        Amount of Income object.
    description : string
        Description of Income object.
    category : enum
        Category of Income object.

    """

    logs.logger.debug(
        "Start to modify the properties of Income object in database "
        "based on the all given properties of Income.")
    try:
        modifiedIncome = session.query(Income.Income).filter(
            Income.Income.id == idOfIncome).one()
        modifiedIncome.registrationDate = registrationDate
        modifiedIncome.dateOfPayment = dateOfPayment
        modifiedIncome.amount = amount
        modifiedIncome.description = description
        modifiedIncome.category = category
        session.commit()
        logs.logger.info(
            "Modify the properties of Income object in database "
            "based on the all given properties of Income.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def ModifyRegistrationDateOfIncome(idOfIncome, registrationDate):
    """Based on the ID of the Income object the registration date
    is modified in database.

    Parameters
    ----------
    idOfIncome : integer
        Id of Income object.
    registrationDate : date
        Registration date of Income object.

    """

    logs.logger.debug(
        "Start to modify registration date of Income based\
             on the ID (%s)." % idOfIncome)
    try:
        modifiedIncome = session.query(Income.Income).filter(
            Income.Income.id == idOfIncome).one()
        modifiedIncome.registrationDate = registrationDate
        session.commit()
        logs.logger.info(
            "Modify registration date of Income based on the ID (%s)." % idOfIncome)
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def ModifyDateOfPaymentOfIncome(idOfIncome, dateOfPayment):
    """Based on the ID of the Income object the date of payment
    is modified in database.

    Parameters
    ----------
    idOfIncome : integer
        Id of Income object.
    dateOfPayment : date
        Payment date of Income object.

    """

    logs.logger.debug(
        "Start to modify payment date of Income based on the\
             ID (%s)." % idOfIncome)
    try:
        modifiedIncome = session.query(Income.Income).filter(
            Income.Income.id == idOfIncome).one()
        modifiedIncome.dateOfPayment = dateOfPayment
        session.commit()
        logs.logger.info(
            "Modify payment date of Income based on the ID(%s)." % idOfIncome)
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def ModifyAmountOfIncome(idOfIncome, amount):
    """Based on the ID of the Income object the amount
    is modified in database.

    Parameters
    ----------
    idOfIncome : integer
        Id of Income object.
    amount : integer
        Amount of Income object.

    """

    logs.logger.debug("Start to modify amount of Income based on the ID (%s)." % idOfIncome)
    try:
        modifiedIncome = session.query(Income.Income).filter(
            Income.Income.id == idOfIncome).one()
        modifiedIncome.amount = amount
        session.commit()
        logs.logger.info(
            "Modify amount of Income based on the ID (%s)." % idOfIncome)
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def ModifyDescriptionOfIncome(idOfIncome, description):
    """Based on the ID of the Income object the description
    is modified in database.

    Parameters
    ----------
    idOfIncome : integer
        Id of Income object.
    description : string
        Description of Income object.

    """

    logs.logger.debug(
        "Start to modify description of Income based on the ID (%s)." % idOfIncome)
    try:
        modifiedIncome = session.query(Income.Income).filter(
            Income.Income.id == idOfIncome).one()
        modifiedIncome.description = description
        session.commit()
        logs.logger.info("Modify description of Income based on the ID (%s)." % idOfIncome)
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def ModifyCategoryOfIncome(idOfIncome, category):
    """Based on the ID of the Income object the category
    is modified in database.

    Parameters
    ----------
    idOfIncome : integer
        Id of Income object.
    category : enum
        Category of Income object.

    """

    logs.logger.debug(
        "Start to modify category of Income based on the ID (%s)." % idOfIncome)
    try:
        modifiedIncome = session.query(Income.Income).filter(
            Income.Income.id == idOfIncome).one()
        modifiedIncome.category = category
        session.commit()
        logs.logger.info(
            "Modify category of Income based on the ID (%s)." % idOfIncome)
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetIncomeByIDFromDB(idOfIncome):
    """Based on the ID of the Income object we get back
    the Income object from database.

    Parameters
    ----------
    idOfIncome : integer
        Id of Income object.

    Returns
    -------
    Income Object
        Income
    """

    logs.logger.debug("Start to get back the Income object from database "
                      "based on ID (%s)." % idOfIncome)
    try:
        searchedIncometByIDFromDB = session.query(
            Income.Income).filter(Income.Income.id == idOfIncome).one()
        logs.logger.info(
            "Get back the Income object from database based on ID (%s)." % idOfIncome)
        return searchedIncometByIDFromDB
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllIncomeByRegistrationDateFromDB(registrationDate):
    """Based on the registration date of the Income objects we get back
    all Income objects from database.

    Parameters
    ----------
    registrationDate : date
        Registration date of Income object.

    Returns
    -------
    List
        List of Income objects.
    """

    logs.logger.debug("Start to get back all Income object from database "
                      "based on registration date (%s)." % registrationDate)
    try:
        searchedIncomeByRegDateFromDB = session.query(Income.Income).filter(
            Income.Income.registrationDate == registrationDate).all()
        logs.logger.info(
            "Get back all Income object from database "
            "based on registration date (%s)." % registrationDate)
        return [item for item in searchedIncomeByRegDateFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllIncomeByDateOfPaymentFromDB(dateOfPayment):
    """Based on the payment date of the Income objects we get back
    all Income objects from database.

    Parameters
    ----------
    dateOfPayment : date
        Payment date of Income object.

    Returns
    -------
    List
        List of Income objects.
    """

    logs.logger.debug(
        "Start to get back all Income object from database "
        "based on payment date (%s)." % dateOfPayment)
    try:
        searchedIncomeByDateOfPaymentFromDB = session.query(
            Income.Income).filter(Income.Income.dateOfPayment == dateOfPayment).all()
        logs.logger.info(
            "Get back all Income object from database based on payment date (%s)." % dateOfPayment)
        return [item for item in searchedIncomeByDateOfPaymentFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllIncomeByAmountFromDB(amount):
    """Based on the amount of the Income objects we get back
    all Income objects from database.

    Parameters
    ----------
    amount : integer
        Amount of Income object.

    Returns
    -------
    List
        List of Income objects.
    """

    logs.logger.debug(
        "Start to get back all Income object from database based on amount (%s)." % amount)
    try:
        searchedIncomeByAmountFromDB = session.query(
            Income.Income).filter(Income.Income.amount == amount).all()
        logs.logger.info(
            "Get back all Income object from database based on amount (%s)." % amount)
        return [item for item in searchedIncomeByAmountFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllIncomeByDescriptionFromDB(description):
    """Based on the description of the Income objects we get back
    all Income objects from database.

    Parameters
    ----------
    description : string
        Description of Income object.

    Returns
    -------
    List
        List of Income objects.
    """

    logs.logger.debug(
        "Start to get back all Income object from database "
        "based on description (%s)." % description)
    try:
        searchedIncomeByDescriptionFromDB = session.query(
            Income.Income).filter(Income.Income.description == description).all()
        logs.logger.info(
            "Get back all Income object from database based on description (%s)." % description)
        return [item for item in searchedIncomeByDescriptionFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllIncomeByCategoryFromDB(category):
    """Based on the category of the Income objects we get back
    all Income objects from database.

    Parameters
    ----------
    category : enum
        Category of Income object.

    Returns
    -------
    List
        List of Income objects.
    """

    logs.logger.debug(
        "Start to get back all Income object from database based on category (%s)." % category)
    try:
        searchedIncomeByCategoryFromDB = session.query(
            Income.Income).filter(Income.Income.category == category).all()
        logs.logger.info(
            "Get back all Income object from database based on category (%s)." % category)
        return [item for item in searchedIncomeByCategoryFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllIncomeByAmountBandFromDB(lowerLimit, upperLimit):
    """Based on an amount band of the Income objects we get back
    all Income objects from database.

    Parameters
    ----------
    lowerLimit : integer
        Lower limit amount of Income objects.
    upperLimit : integer
        Upper limit amount of Income objects.

    Returns
    -------
    List
        List of Income objects.
    """

    logs.logger.debug("Start to get back all Income object from database "
                      "based on amount band (%s < < %s)." % (lowerLimit, upperLimit))
    try:
        searchedIncomeByAmountBandFromDB = session.query(
            Income.Income).filter(Income.Income.amount >= lowerLimit, Income.Income.amount <= upperLimit).all()
        logs.logger.info(
            "Get back all Income object from database based on\
                 amount band (%s < < %s)." % (lowerLimit, upperLimit))
        return [item for item in searchedIncomeByAmountBandFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllIncomeByDateOfPaymentBandFromDB(startDate, endDate):
    """Based on payment date band of the Income objects we get back
    all Income objects from database.

    Parameters
    ----------
    startDate : date
        Start date of payment.
    endDate : date
        Start date of payment.

    Returns
    -------
    List
        List of Income objects.
    """

    logs.logger.debug(
        "Start to get back all Income object from database "
        "based on payment date band (%s < < %s)." % (startDate, endDate))
    try:
        searchedIncomeByDateOfPaymentBandFromDB = session.query(
            Income.Income).filter(Income.Income.dateOfPayment >= startDate, Income.Income.dateOfPayment <= endDate).all()
        logs.logger.info(
            "Get back all Income object from database "
            "based on payment date band (%s < < %s)." % (startDate, endDate))
        return [item for item in searchedIncomeByDateOfPaymentBandFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllRegistrationDateOfIncome():
    """All registration date of Income objects is got back from database.

    Returns
    -------
    List
        List of Registration dates of Income objects.
    """

    logs.logger.debug("Start to get back all registration date of "
                      "Income objects from database.")
    try:
        searchedIncomeItems = session.query(Income.Income).all()
        logs.logger.info(
            "Get back all registration date of Income objects from database.")
        return [IncomeItems.registrationDate for IncomeItems in searchedIncomeItems]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDateOfPaymentOfIncome():
    """All payment date of Income objects is got back from database.

    Returns
    -------
    List
        List of Payment dates of Income objects.
    """

    logs.logger.debug(
        "Start to get back all payment date of Income objects from database.")
    try:
        searchedIncomeItems = session.query(Income.Income).all()
        logs.logger.info(
            "Get back all payment date of Income objects from database.")
        return [IncomeItems.dateOfPayment for IncomeItems in searchedIncomeItems]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllAmountOfIncome():
    """All amounts of Income objects is got back from database.

    Returns
    -------
    List
        List of Amounts of Income objects.
    """

    logs.logger.debug("Start to get back all amounts of "
                      "Income objects from database.")
    try:
        searchedIncomeItems = session.query(Income.Income).all()
        logs.logger.info("Get back all amounts of Income\
             objects from database.")
        return [IncomeItems.amount for IncomeItems in searchedIncomeItems]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDescriptionOfIncome():
    """All descriptions of Income objects is got back from database.

    Returns
    -------
    List
        List of Descriptions of Income objects.
    """

    logs.logger.debug(
        "Start to get back all descriptions of Income objects from database.")
    try:
        searchedIncomeItems = session.query(Income.Income).all()
        logs.logger.info(
            "Get back all descriptions of Income objects from database.")
        return [IncomeItems.description for IncomeItems in searchedIncomeItems]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllCategoryOfIncome():
    """All categories of Income objects is got back from database.

    Returns
    -------
    List
        List of Categories of Income objects.
    """

    logs.logger.debug(
        "Start to get back all categories of Income objects from database.")
    try:
        searchedIncomeItems = session.query(Income.Income).all()
        logs.logger.info(
            "Get back all categories of Income objects from database.")
        return [IncomeItems.category for IncomeItems in searchedIncomeItems]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDifferentRegistrationDateOfIncome():
    """All different registration date of Income objects is got back from database.

    Returns
    -------
    List
        List of Registration dates of Income objects.
    """

    logs.logger.debug(
        "Start to get back all different registration date of "
        "Income objects from database.")
    try:
        ListOfAllDifferentRegistrationDateOfIncome = []
        searchedIncomeItems = GetAllRegistrationDateOfIncome()
        for item in searchedIncomeItems:
            if item not in ListOfAllDifferentRegistrationDateOfIncome:
                ListOfAllDifferentRegistrationDateOfIncome.append(item)
        logs.logger.info(
            "Get back all different registration date of "
            "Income objects from database.")
        return ListOfAllDifferentRegistrationDateOfIncome
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDifferentDateOfPaymentOfIncome():
    """All different payment date of Income objects is got back from database.

    Returns
    -------
    List
        List of Payment dates of Income objects.
    """

    logs.logger.debug(
        "Start to get back all different payment date of "
        "Income objects from database.")
    try:
        ListOfAllDifferentDateOfPaymentOfIncome = []
        searchedIncomeItems = GetAllDateOfPaymentOfIncome()
        for item in searchedIncomeItems:
            if item not in ListOfAllDifferentDateOfPaymentOfIncome:
                ListOfAllDifferentDateOfPaymentOfIncome.append(item)
        logs.logger.info(
            "Get back all different payment date of "
            "Income objects from database.")
        return ListOfAllDifferentDateOfPaymentOfIncome
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDifferentAmountOfIncome():
    """All different amounts of Income objects is got back from database.

    Returns
    -------
    List
        List of Amounts of Income objects.
    """

    logs.logger.debug(
        "Start to get back all different amount of "
        "Income objects from database.")
    try:
        ListOfAllDifferentAmountOfIncome = []
        searchedIncomeItems = GetAllAmountOfIncome()
        for item in searchedIncomeItems:
            if item not in ListOfAllDifferentAmountOfIncome:
                ListOfAllDifferentAmountOfIncome.append(item)
        logs.logger.info(
            "Get back all different amount of Income objects from database.")
        return ListOfAllDifferentAmountOfIncome
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDifferentDescriptionOfIncome():
    """All different descriptions of Income objects is got back from database.

    Returns
    -------
    List
        List of Descriptions of Income objects.
    """

    logs.logger.debug(
        "Start to get back all different description of "
        "Income objects from database.")
    try:
        ListOfAllDifferentDescriptionOfIncome = []
        searchedIncomeItems = GetAllDescriptionOfIncome()
        for item in searchedIncomeItems:
            if item not in ListOfAllDifferentDescriptionOfIncome:
                ListOfAllDifferentDescriptionOfIncome.append(item)
        logs.logger.info(
            "Start to get back all different description of "
            "Income objects from database.")
        return ListOfAllDifferentDescriptionOfIncome
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDifferentCategoryOfIncome():
    """All different categories of Income objects is got back from database.

    Returns
    -------
    List
        List of Categories of Income objects.
    """

    logs.logger.debug(
        "Start to get back all different categories of "
        "Income objects from database.")
    try:
        ListOfAllDifferentCategoryOfIncome = []
        searchedIncomeItems = GetAllCategoryOfIncome()
        for item in searchedIncomeItems:
            if item not in ListOfAllDifferentCategoryOfIncome:
                ListOfAllDifferentCategoryOfIncome.append(item)
        logs.logger.info(
            "Get back all different categories of "
            "Income objects from database.")
        return ListOfAllDifferentCategoryOfIncome
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllIncomesFromDB():
    """All Income objects is got back from database.

    Returns
    -------
    List
        List of Income objects.
    """

    logs.logger.debug("Start to get back all Income objects from database.")
    try:
        ListOfAllIncome = session.query(Income.Income).all()
        logs.logger.info("Get back all Income objects from database.")
        return [item for item in ListOfAllIncome]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumTotalIncome():
    """Adds all amount of Income objects.

    Returns
    -------
    Integer
        Summarize amount of all Income objects from database.
    """

    logs.logger.debug("Start to add all amount of Income objects.")
    try:
        sumTotal = 0
        for item in GetAllAmountOfIncome():
            sumTotal += item
        logs.logger.info("Add all amount of Income objects.")
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumIncomeByCategory(category):
    """Based on the category adds all amount of Income objects.

    Parameters
    ----------
    category : enum
        Category of Income object.

    Returns
    -------
    Integer
        Summarize amount of all Income objects with the same category
        from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Income objects based on category (%s)." % category)
    try:
        searchedIncomeByCategoryFromDB = GetAllIncomeByCategoryFromDB(category)
        sumTotal = 0
        for item in searchedIncomeByCategoryFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Based on the category (%s) adds all amount of Income objects." % category)
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumIncomeByDay(dateOfPayment):
    """Based on the payment date adds all amount of Income objects.

    Parameters
    ----------
    dateOfPayment : date
        Payment date of Income objects.

    Returns
    -------
    Integer
        Summarize amount of all Income objects with the same payment date
        from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Income objects based on the payment date (%s)." % dateOfPayment)
    try:
        searchedIncomeByDayFromDB = GetAllIncomeByDateOfPaymentFromDB(
            dateOfPayment)
        sumTotal = 0
        for item in searchedIncomeByDayFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Based on the payment date (%s) adds all amount of Income objects." % dateOfPayment)
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumIncomeByMonth(year, numberOfMonth):
    """Based on a defined month adds all amount of Income objects.

    Parameters
    ----------
    year : integer
        Year of payment date.
    numberOfMonth : integer
        Month of payment date (in number).

    Returns
    -------
    Integer
        Summarize amount of all Income objects with the same month of
        payment date from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Income objects based on a defined month (%s / %s)." % (year, numberOfMonth))
    try:
        num_days = calendar.monthrange(year, numberOfMonth)[1]
        searchedIncomeByMonthFromDB = GetAllIncomeByDateOfPaymentBandFromDB(
            date(year, numberOfMonth, 1), date(year, numberOfMonth, num_days))
        sumTotal = 0
        for item in searchedIncomeByMonthFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Based on a defined month (%s / %s) adds all amount of Income objects." % (year, numberOfMonth))
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumIncomeByQuarter(year, quarter):
    """Based on a defined quarter adds all amount of Income objects.

    Parameters
    ----------
    year : integer
        Year of payment date.
    quarter : integer
        Quarter of payment date (in number).

    Returns
    -------
    Integer
        Summarize amount of all Income objects with the same quarter of
        payment date from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Income objects based on a defined quarter (%s . %s)." % (year, quarter))
    try:
        first_month_of_quarter = 3 * quarter - 2
        last_month_of_quarter = 3 * quarter
        date_of_first_day_of_quarter = date(year, first_month_of_quarter, 1)
        date_of_last_day_of_quarter = date(
            year, last_month_of_quarter, calendar.monthrange(
                year, last_month_of_quarter)[1])
        searchedIncomeByQuarterFromDB = GetAllIncomeByDateOfPaymentBandFromDB(
            date_of_first_day_of_quarter, date_of_last_day_of_quarter)
        sumTotal = 0
        for item in searchedIncomeByQuarterFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Based on a defined quarter (%s . %s) adds all amount of Income objects." % (year, quarter))
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumIncomeByYear(year):
    """Based on a defined year adds all amount of Income objects.

    Parameters
    ----------
    year : integer
        Year of payment date.

    Returns
    -------
    Integer
        Summarize amount of all Income objects with the same year of
        payment date from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Income objects based on a defined year (%s)." % year)
    try:
        first_day_of_year = date(year, 1, 31)
        last_day_of_year = date(year, 12, 31)
        searchedIncomeByYearFromDB = GetAllIncomeByDateOfPaymentBandFromDB(
            first_day_of_year, last_day_of_year)
        sumTotal = 0
        for item in searchedIncomeByYearFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Based on a defined year (%s) adds all amount of Income objects." % year)
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumIncomeByBetweenDates(startDate, endDate):
    """Between two dates adds all amount of Income objects.

    Parameters
    ----------
    startDate : date
        From this date.
    endDate : date
        Until this date.

    Returns
    -------
    Integer
        Summarize amount of all Income objects with the same year of
        payment date from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Income objects between two dates (%s - %s)." % (startDate, endDate))
    try:
        searchedIncomeByBetweenDatesFromDB = GetAllIncomeByDateOfPaymentBandFromDB(
            startDate, endDate)
        sumTotal = 0
        for item in searchedIncomeByBetweenDatesFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Between two dates (%s - %s) adds all amount of Income objects." % (startDate, endDate))
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumIncomeByDayPerCategory(day, category):
    """Based on the payment date and on the category adds all amount of
    Income objects.

    Parameters
    ----------
    day : date
        Payment date of Income objects.
    category : string
        Category of Income object.

    Returns
    -------
    Integer
        Summarize amount of all Income objects with the same payment date
        and category from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Income objects based on the payment date (%s)\
             and on the category (%s)." % (day, category))
    try:
        searchedIncomeByDayPerCategoryFromDB = session.query(
            Income.Income).filter(Income.Income.dateOfPayment == day).filter(
                Income.Income.category == category).all()
        sumTotal = 0
        for item in searchedIncomeByDayPerCategoryFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Based on the payment date (%s) and on the category (%s) adds all amount of Income objects." % (day, category))
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumIncomeByMonthPerCategory(year, numberOfMonth, category):
    """Based on the month of payment date and on the category adds all amount of
    Income objects.

    Parameters
    ----------
    year : integer
        Year of payment date.
    numberOfMonth : integer
        Number of month of payment date.
    category : string
        Category of Income object.

    Returns
    -------
    Integer
        Summarize amount of all Income objects with the same month of
        payment date and category from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Income objects based on\
             the month of payment date (%s / %s) and on the category (%s)." % (year, numberOfMonth, category))
    try:
        num_days = calendar.monthrange(year, numberOfMonth)[1]
        searchedIncomeByMonthFromDB = GetAllIncomeByDateOfPaymentBandFromDB(
            date(year, numberOfMonth, 1), date(year, numberOfMonth, num_days))
        sumTotal = 0
        for item in searchedIncomeByMonthFromDB:
            if item.category.value == category:
                sumTotal += item.amount
        logs.logger.info(
            "Based on the month of payment date (%s / %s) and on the category (%s)\
                 adds all amount of Income objects." % (year, numberOfMonth, category))
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumIncomeByQuarterPerCategory(year, quarter, category):
    """Based on the quarter of payment date and on the category adds all amount of
    Income objects.

    Parameters
    ----------
    year : integer
        Year of payment date.
    quarter : integer
        Number of quarter of payment date.
    category : string
        Category of Income object.

    Returns
    -------
    Integer
        Summarize amount of all Income objects with the same quarter of
        payment date and category from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Income objects based\
             on the quarter of payment date (%s / %s) and on the category (%s)." % (year, quarter, category))
    try:
        first_month_of_quarter = 3 * quarter - 2
        last_month_of_quarter = 3 * quarter
        date_of_first_day_of_quarter = date(year, first_month_of_quarter, 1)
        date_of_last_day_of_quarter = date(
            year, last_month_of_quarter, calendar.monthrange(
                year, last_month_of_quarter)[1])
        searchedIncomeByQuarterFromDB = GetAllIncomeByDateOfPaymentBandFromDB(
            date_of_first_day_of_quarter, date_of_last_day_of_quarter)
        sumTotal = 0
        for item in searchedIncomeByQuarterFromDB:
            if item.category.value == category:
                sumTotal += item.amount
        logs.logger.info(
            "Based on the quarter of payment date (%s / %s) and on the category (%s)\
                 adds all amount of Income\
                      objects." % (year, quarter, category))
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumIncomeByYearPerCategory(year, category):
    """Based on the year of payment date and on the category adds all amount of
    Income objects.

    Parameters
    ----------
    year : integer
        Year of payment date.
    category : string
        Category of Income object.

    Returns
    -------
    Integer
        Summarize amount of all Income objects with the same year of
        payment date and category from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Income objects based\
             on the year of payment (%s) date and on the category (%s)." % (year, category))
    try:
        first_day_of_year = date(year, 1, 31)
        last_day_of_year = date(year, 12, 31)
        searchedIncomeByYearFromDB = GetAllIncomeByDateOfPaymentBandFromDB(
            first_day_of_year, last_day_of_year)
        sumTotal = 0
        for item in searchedIncomeByYearFromDB:
            if item.category.value == category:
                sumTotal += item.amount
        logs.logger.info(
            "Based on the year of payment date (%s) and\
                 on the category (%s) adds all amount of Income objects." % (year, category))
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumIncomeByBetweenDatesPerCategory(startDate, endDate, category):
    """Between two payment date and on the category adds all amount of
    Income objects.

    Parameters
    ----------
    startDate : date
        Start date of payment.
    endDate : date
        End date of payment.
    category : string
        Category of Income objects.

    Returns
    -------
    Integer
        Summarize amount of all Income objects between two payment date
        and category from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Income objects\
             between two payment date (%s - %s) and on the category (%s)" % (startDate, endDate, category))
    try:
        searchedIncomeByBetweenDatesFromDB = GetAllIncomeByDateOfPaymentBandFromDB(
            startDate, endDate)
        sumTotal = 0
        for item in searchedIncomeByBetweenDatesFromDB:
            if item.category.value == category:
                sumTotal += item.amount
        logs.logger.info(
            "Between two payment date (%s - %s) and\
                 on the category (%s) adds all amount of Income objects." % (startDate, endDate, category))
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SearcherInDescription(input):
    """Using this method you can search in description.

    Parameters
    ----------
    input : string
        Searched string in description.

    Returns
    -------
    List
        List of Income objects where the descriptions conain
        the searched string.
    """

    logs.logger.debug(
        "Start to search in description based on userinput (%s)." % input)
    try:
        NormalizedMySearchedWords = unicodedata.normalize(
            'NFKD', input.upper()).encode('ASCII', 'ignore')
        ListOfAllIncome = GetAllIncomesFromDB()
        ListOfSearchedCosts = []
        for item in ListOfAllIncome:
            NormalizedMyText = unicodedata.normalize(
                'NFKD', item.description.upper()).encode('ASCII', 'ignore')
            if NormalizedMyText.__contains__(NormalizedMySearchedWords):
                ListOfSearchedCosts.append(item)
        logs.logger.info(
            "You search in description based on userinput (%s)." % input)
        return ListOfSearchedCosts
    except Exception as e:
        logs.logger.error(e, exc_info=True)
