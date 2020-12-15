import sqlalchemy as sqla
import datetime
import calendar
from datetime import date
import unicodedata

import MyBudgetManager.MyBudgetManager.Models.Cost as Cost
from MyBudgetManager.MyBudgetManager.Models.base import session
import MyBudgetManager.MyBudgetManager.Log.logs as logs


def PrintAllCosts():
    """After queries of all costs from database this method print the details
    (id, reg.date, date of payment, amount, description, category)
    of the costs to the consol.

    """

    logs.logger.debug("After queries of all costs from database start to print"
                      " the details (id, reg.date, date of payment, amount,"
                      " description, category) of the costs to the consol.")
    try:
        printedCosts = session.query(Cost.Cost).all()
        for cost in printedCosts:
            print(
                f'{cost.id}\t{cost.registrationDate}\t{cost.dateOfPayment} \
                    \t{cost.amount}\t{cost.description}\t{cost.category.value}')
        logs.logger.info("After queries of all costs from database print"
                         " the details (id, reg.date, date of payment, amount,"
                         " description, category) of the costs to the consol.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def PrintCosts(CostList):
    """Print all costs based on the given costs list parameter.

    Parameters
    ----------
    CostList : list
        List of Costs

    """

    logs.logger.debug(
        "Start to print all costs based on the given costs list parameter.")
    try:
        for cost in CostList:
            print(
                f'{cost.id}\t{cost.registrationDate}\t{cost.dateOfPayment} \
                    \t{cost.amount}\t{cost.description}\t{cost.category.value}')
        logs.logger.info(
            "Print all costs based on the given costs list parameter.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def AddCost(Cost):
    """Add Cost object to the database.

    Parameters
    ----------
    Cost : object
        Cost object.

    """

    logs.logger.debug("Start to add Cost object to the database.")
    try:
        session.add(Cost)
        session.commit()
        logs.logger.info("Add Cost object to the database.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def DeleteCost(idOfCost):
    """Based on Id parameter of the Cost object this method deletes the Cost
    object from database.

    Parameters
    ----------
    idOfCost : integer
        Id of the Cost object.

    """

    logs.logger.debug(
        "Start to deletes the Cost object from database "
        "based on Id parameter.")
    try:
        deletedCost = session.query(Cost.Cost).filter(
            Cost.Cost.id == idOfCost).one()
        session.delete(deletedCost)
        session.commit()
        logs.logger.info("Deletes the Cost object from database "
                         "based on Id parameter.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def ModifyTheFullRowOfCost(idOfCost, registrationDate, dateOfPayment,
                           amount, description, category):
    """Based on the all given properties of Cost as parameters this method
    modifys the properties of Cost object in database.

    Parameters
    ----------
    idOfCost : integer
        Id of Cost object.
    registrationDate : date
        Registration date of Cost object.
    dateOfPayment : date
        Payment date of Cost object.
    amount : integer
        Amount of Cost object.
    description : string
        Description of Cost object.
    category : enum
        Category of Cost object.

    """

    logs.logger.debug(
        "Start to modify the properties of Cost object in database "
        "based on the all given properties of Cost.")
    try:
        modifiedCost = session.query(Cost.Cost).filter(
            Cost.Cost.id == idOfCost).one()
        modifiedCost.registrationDate = registrationDate
        modifiedCost.dateOfPayment = dateOfPayment
        modifiedCost.amount = amount
        modifiedCost.description = description
        modifiedCost.category = category
        session.commit()
        logs.logger.info(
            "Modify the properties of Cost object in database "
            "based on the all given properties of Cost.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def ModifyRegistrationDateOfCost(idOfCost, registrationDate):
    """Based on the ID of the Cost object the registration date
    is modified in database.

    Parameters
    ----------
    idOfCost : integer
        Id of Cost object.
    registrationDate : date
        Registration date of Cost object.

    """

    logs.logger.debug(
        "Start to modify registration date of Cost based on the ID.")
    try:
        modifiedCost = session.query(Cost.Cost).filter(
            Cost.Cost.id == idOfCost).one()
        modifiedCost.registrationDate = registrationDate
        session.commit()
        logs.logger.info("Modify registration date of Cost based on the ID.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def ModifyDateOfPaymentOfCost(idOfCost, dateOfPayment):
    """Based on the ID of the Cost object the date of payment
    is modified in database.

    Parameters
    ----------
    idOfCost : integer
        Id of Cost object.
    dateOfPayment : date
        Payment date of Cost object.

    """

    logs.logger.debug(
        "Start to modify payment date of Cost based on the ID.")
    try:
        modifiedCost = session.query(Cost.Cost).filter(
            Cost.Cost.id == idOfCost).one()
        modifiedCost.dateOfPayment = dateOfPayment
        session.commit()
        logs.logger.info(
            "Modify payment date of Cost based on the ID.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def ModifyAmountOfCost(idOfCost, amount):
    """Based on the ID of the Cost object the amount
    is modified in database.

    Parameters
    ----------
    idOfCost : integer
        Id of Cost object.
    amount : integer
        Amount of Cost object.

    """

    logs.logger.debug("Start to modify amount of Cost based on the ID.")
    try:
        modifiedCost = session.query(Cost.Cost).filter(
            Cost.Cost.id == idOfCost).one()
        modifiedCost.amount = amount
        session.commit()
        logs.logger.info("Modify amount of Cost based on the ID.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def ModifyDescriptionOfCost(idOfCost, description):
    """Based on the ID of the Cost object the description
    is modified in database.

    Parameters
    ----------
    idOfCost : integer
        Id of Cost object.
    description : string
        Description of Cost object.

    """

    logs.logger.debug("Start to modify description of Cost based on the ID.")
    try:
        modifiedCost = session.query(Cost.Cost).filter(
            Cost.Cost.id == idOfCost).one()
        modifiedCost.description = description
        session.commit()
        logs.logger.info("Modify description of Cost based on the ID.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def ModifyCategoryOfCost(idOfCost, category):
    """Based on the ID of the Cost object the category
    is modified in database.

    Parameters
    ----------
    idOfCost : integer
        Id of Cost object.
    category : enum
        Category of Cost object.

    """

    logs.logger.debug("Start to modify category of Cost based on the ID.")
    try:
        modifiedCost = session.query(Cost.Cost).filter(
            Cost.Cost.id == idOfCost).one()
        modifiedCost.category = category
        session.commit()
        logs.logger.info("Modify category of Cost based on the ID.")
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetCostByIDFromDB(idOfCost):
    """Based on the ID of the Cost object we get back
    the Cost object from database.

    Parameters
    ----------
    idOfCost : integer
        Id of Cost object.

    Returns
    -------
    Cost Object
        Cost
    """

    logs.logger.debug("Start to get back the Cost object from database "
                      "based on ID.")
    try:
        searchedCostByIDFromDB = session.query(
            Cost.Cost).filter(Cost.Cost.id == idOfCost).one()
        logs.logger.info("Get back the Cost object from database based on ID.")
        return searchedCostByIDFromDB
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllCostByRegistrationDateFromDB(registrationDate):
    """Based on the registration date of the Cost objects we get back
    all Cost objects from database.

    Parameters
    ----------
    registrationDate : date
        Registration date of Cost object.

    Returns
    -------
    List
        List of Cost objects.
    """

    logs.logger.debug("Start to get back all Cost object from database "
                      "based on registration date.")
    try:
        searchedCostByRegDateFromDB = session.query(Cost.Cost).filter(
            Cost.Cost.registrationDate == registrationDate).all()
        logs.logger.info(
            "Get back all Cost object from database "
            "based on registration date.")
        return [item for item in searchedCostByRegDateFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllCostByDateOfPaymentFromDB(dateOfPayment):
    """Based on the payment date of the Cost objects we get back
    all Cost objects from database.

    Parameters
    ----------
    dateOfPayment : date
        Payment date of Cost object.

    Returns
    -------
    List
        List of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all Cost object from database "
        "based on payment date.")
    try:
        searchedCostByDateOfPaymentFromDB = session.query(
            Cost.Cost).filter(Cost.Cost.dateOfPayment == dateOfPayment).all()
        logs.logger.info(
            "Get back all Cost object from database based on payment date.")
        return [item for item in searchedCostByDateOfPaymentFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllCostByAmountFromDB(amount):
    """Based on the amount of the Cost objects we get back
    all Cost objects from database.

    Parameters
    ----------
    amount : integer
        Amount of Cost object.

    Returns
    -------
    List
        List of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all Cost object from database based on amount.")
    try:
        searchedCostByAmountFromDB = session.query(
            Cost.Cost).filter(Cost.Cost.amount == amount).all()
        logs.logger.info(
            "Get back all Cost object from database based on amount.")
        return [item for item in searchedCostByAmountFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllCostByDescriptionFromDB(description):
    """Based on the description of the Cost objects we get back
    all Cost objects from database.

    Parameters
    ----------
    description : string
        Description of Cost object.

    Returns
    -------
    List
        List of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all Cost object from database "
        "based on description.")
    try:
        searchedCostByDescriptionFromDB = session.query(
            Cost.Cost).filter(Cost.Cost.description == description).all()
        logs.logger.info(
            "Get back all Cost object from database based on description.")
        return [item for item in searchedCostByDescriptionFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllCostByCategoryFromDB(category):
    """Based on the category of the Cost objects we get back
    all Cost objects from database.

    Parameters
    ----------
    category : enum
        Category of Cost object.

    Returns
    -------
    List
        List of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all Cost object from database based on category.")
    try:
        searchedCostByCategoryFromDB = session.query(
            Cost.Cost).filter(Cost.Cost.category == category).all()
        logs.logger.info(
            "Get back all Cost object from database based on category.")
        return [item for item in searchedCostByCategoryFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllCostByAmountBandFromDB(lowerLimit, upperLimit):
    """Based on an amount band of the Cost objects we get back
    all Cost objects from database.

    Parameters
    ----------
    lowerLimit : integer
        Lower limit amount of Cost objects.
    upperLimit : integer
        Upper limit amount of Cost objects.

    Returns
    -------
    List
        List of Cost objects.
    """

    logs.logger.debug("Start to get back all Cost object from database\
        based on amount band.")
    try:
        searchedCostByAmountBandFromDB = session.query(
            Cost.Cost).filter(Cost.Cost.amount >= lowerLimit, Cost.Cost.amount <= upperLimit).all()
        logs.logger.info(
            "Get back all Cost object from database based on amount band.")
        return [item for item in searchedCostByAmountBandFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllCostByDateOfPaymentBandFromDB(startDate, endDate):
    """Based on payment date band of the Cost objects we get back
    all Cost objects from database.

    Parameters
    ----------
    startDate : date
        Start date of payment.
    endDate : date
        Start date of payment.

    Returns
    -------
    List
        List of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all Cost object from database "
        "based on payment date band.")
    try:
        searchedCostByDateOfPaymentBandFromDB = session.query(
            Cost.Cost).filter(Cost.Cost.dateOfPayment >= startDate, Cost.Cost.dateOfPayment <= endDate).all()
        logs.logger.info(
            "Get back all Cost object from database "
            "based on payment date band.")
        return [item for item in searchedCostByDateOfPaymentBandFromDB]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllRegistrationDateOfCost():
    """All registration date of Cost objects is got back from database.

    Returns
    -------
    List
        List of Registration dates of Cost objects.
    """

    logs.logger.debug("Start to get back all registration date of\
         Cost objects from database.")
    try:
        searchedCostsItems = session.query(Cost.Cost).all()
        logs.logger.info(
            "Get back all registration date of Cost objects from database.")
        return [CostItems.registrationDate for CostItems in searchedCostsItems]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDateOfPaymentOfCost():
    """All payment date of Cost objects is got back from database.

    Returns
    -------
    List
        List of Payment dates of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all payment date of Cost objects from database.")
    try:
        searchedCostsItems = session.query(Cost.Cost).all()
        logs.logger.info(
            "Get back all payment date of Cost objects from database.")
        return [CostItems.dateOfPayment for CostItems in searchedCostsItems]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllAmountOfCost():
    """All amounts of Cost objects is got back from database.

    Returns
    -------
    List
        List of Amounts of Cost objects.
    """

    logs.logger.debug("Start to get back all amounts of\
        Cost objects from database.")
    try:
        searchedCostsItems = session.query(Cost.Cost).all()
        logs.logger.info("Get back all amounts of Cost objects from database.")
        return [CostItems.amount for CostItems in searchedCostsItems]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDescriptionOfCost():
    """All descriptions of Cost objects is got back from database.

    Returns
    -------
    List
        List of Descriptions of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all descriptions of Cost objects from database.")
    try:
        searchedCostsItems = session.query(Cost.Cost).all()
        logs.logger.info(
            "Get back all descriptions of Cost objects from database.")
        return [CostItems.description for CostItems in searchedCostsItems]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllCategoryOfCost():
    """All categories of Cost objects is got back from database.

    Returns
    -------
    List
        List of Categories of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all categories of Cost objects from database.")
    try:
        searchedCostsItems = session.query(Cost.Cost).all()
        logs.logger.info(
            "Get back all categories of Cost objects from database.")
        return [CostItems.category for CostItems in searchedCostsItems]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDifferentRegistrationDateOfCost():
    """All different registration date of Cost objects is got back from database.

    Returns
    -------
    List
        List of Registration dates of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all different registration date of "
        "Cost objects from database.")
    try:
        ListOfAllDifferentRegistrationDateOfCost = []
        searchedCostsItems = GetAllRegistrationDateOfCost()
        for item in searchedCostsItems:
            if item not in ListOfAllDifferentRegistrationDateOfCost:
                ListOfAllDifferentRegistrationDateOfCost.append(item)
        logs.logger.info(
            "Get back all different registration date of "
            "Cost objects from database.")
        return ListOfAllDifferentRegistrationDateOfCost
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDifferentDateOfPaymentOfCost():
    """All different payment date of Cost objects is got back from database.

    Returns
    -------
    List
        List of Payment dates of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all different payment date of "
        "Cost objects from database.")
    try:
        ListOfAllDifferentDateOfPaymentOfCost = []
        searchedCostsItems = GetAllDateOfPaymentOfCost()
        for item in searchedCostsItems:
            if item not in ListOfAllDifferentDateOfPaymentOfCost:
                ListOfAllDifferentDateOfPaymentOfCost.append(item)
        logs.logger.info(
            "Get back all different payment date of "
            "Cost objects from database.")
        return ListOfAllDifferentDateOfPaymentOfCost
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDifferentAmountOfCost():
    """All different amounts of Cost objects is got back from database.

    Returns
    -------
    List
        List of Amounts of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all different amount of "
        "Cost objects from database.")
    try:
        ListOfAllDifferentAmountOfCost = []
        searchedCostsItems = GetAllAmountOfCost()
        for item in searchedCostsItems:
            if item not in ListOfAllDifferentAmountOfCost:
                ListOfAllDifferentAmountOfCost.append(item)
        logs.logger.info(
            "Get back all different amount of Cost objects from database.")
        return ListOfAllDifferentAmountOfCost
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDifferentDescriptionOfCost():
    """All different descriptions of Cost objects is got back from database.

    Returns
    -------
    List
        List of Descriptions of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all different description of "
        "Cost objects from database.")
    try:
        ListOfAllDifferentDescriptionOfCost = []
        searchedCostsItems = GetAllDescriptionOfCost()
        for item in searchedCostsItems:
            if item not in ListOfAllDifferentDescriptionOfCost:
                ListOfAllDifferentDescriptionOfCost.append(item)
        logs.logger.info(
            "Start to get back all different description of "
            "Cost objects from database.")
        return ListOfAllDifferentDescriptionOfCost
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllDifferentCategoryOfCost():
    """All different categories of Cost objects is got back from database.

    Returns
    -------
    List
        List of Categories of Cost objects.
    """

    logs.logger.debug(
        "Start to get back all different categories of "
        "Cost objects from database.")
    try:
        ListOfAllDifferentCategoryOfCost = []
        searchedCostsItems = GetAllCategoryOfCost()
        for item in searchedCostsItems:
            if item not in ListOfAllDifferentCategoryOfCost:
                ListOfAllDifferentCategoryOfCost.append(item)
        logs.logger.info(
            "Get back all different categories of "
            "Cost objects from database.")
        return ListOfAllDifferentCategoryOfCost
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def GetAllCostsFromDB():
    """All Cost objects is got back from database.

    Returns
    -------
    List
        List of Cost objects.
    """

    logs.logger.debug("Start to get back all Cost objects from database.")
    try:
        ListOfAllCost = session.query(Cost.Cost).all()
        logs.logger.info("Get back all Cost objects from database.")
        return [item for item in ListOfAllCost]
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumTotalCost():
    """Adds all amount of Cost objects.

    Returns
    -------
    Integer
        Summarize amount of all Cost objects from database.
    """

    logs.logger.debug("Start to add all amount of Cost objects.")
    try:
        sumTotal = 0
        for item in GetAllAmountOfCost():
            sumTotal += item
        logs.logger.info("Add all amount of Cost objects.")
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumCostByCategory(category):
    """Based on the category adds all amount of Cost objects.

    Parameters
    ----------
    category : enum
        Category of Cost object.

    Returns
    -------
    Integer
        Summarize amount of all Cost objects with the same category
        from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Cost objects based on category.")
    try:
        searchedCostByCategoryFromDB = GetAllCostByCategoryFromDB(category)
        sumTotal = 0
        for item in searchedCostByCategoryFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Based on the category adds all amount of Cost objects.")
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumCostByDay(dateOfPayment):
    """Based on the payment date adds all amount of Cost objects.

    Parameters
    ----------
    dateOfPayment : date
        Payment date of Cost objects.

    Returns
    -------
    Integer
        Summarize amount of all Cost objects with the same payment date
        from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Cost objects based on the payment date.")
    try:
        searchedCostByDayFromDB = GetAllCostByDateOfPaymentFromDB(dateOfPayment)
        sumTotal = 0
        for item in searchedCostByDayFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Based on the payment date adds all amount of Cost objects.")
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumCostByMonth(year, numberOfMonth):
    """Based on a defined month adds all amount of Cost objects.

    Parameters
    ----------
    year : integer
        Year of payment date.
    numberOfMonth : integer
        Month of payment date (in number).

    Returns
    -------
    Integer
        Summarize amount of all Cost objects with the same month of payment date
        from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Cost objects based on a defined month.")
    try:
        num_days = calendar.monthrange(year, numberOfMonth)[1]
        searchedCostByMonthFromDB = GetAllCostByDateOfPaymentBandFromDB(
            date(year, numberOfMonth, 1), date(year, numberOfMonth, num_days))
        sumTotal = 0
        for item in searchedCostByMonthFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Based on a defined month adds all amount of Cost objects.")
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumCostByQuarter(year, quarter):
    """Based on a defined quarter adds all amount of Cost objects.

    Parameters
    ----------
    year : integer
        Year of payment date.
    quarter : integer
        Quarter of payment date (in number).

    Returns
    -------
    Integer
        Summarize amount of all Cost objects with the same quarter of
        payment date from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Cost objects based on a defined quarter.")
    try:
        first_month_of_quarter = 3 * quarter - 2
        last_month_of_quarter = 3 * quarter
        date_of_first_day_of_quarter = date(year, first_month_of_quarter, 1)
        date_of_last_day_of_quarter = date(
            year, last_month_of_quarter, calendar.monthrange(
                year, last_month_of_quarter)[1])
        searchedCostByQuarterFromDB = GetAllCostByDateOfPaymentBandFromDB(
            date_of_first_day_of_quarter, date_of_last_day_of_quarter)
        sumTotal = 0
        for item in searchedCostByQuarterFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Based on a defined quarter adds all amount of Cost objects.")
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumCostByYear(year):
    """Based on a defined year adds all amount of Cost objects.

    Parameters
    ----------
    year : integer
        Year of payment date.

    Returns
    -------
    Integer
        Summarize amount of all Cost objects with the same year of
        payment date from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Cost objects based on a defined year.")
    try:
        first_day_of_year = date(year, 1, 31)
        last_day_of_year = date(year, 12, 31)
        searchedCostByYearFromDB = GetAllCostByDateOfPaymentBandFromDB(
            first_day_of_year, last_day_of_year)
        sumTotal = 0
        for item in searchedCostByYearFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Based on a defined year adds all amount of Cost objects.")
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumCostByBetweenDates(startDate, endDate):
    """Between two dates adds all amount of Cost objects.

    Parameters
    ----------
    startDate : date
        From this date.
    endDate : date
        Until this date.

    Returns
    -------
    Integer
        Summarize amount of all Cost objects with the same year of
        payment date from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Cost objects between two dates.")
    try:
        searchedCostByBetweenDatesFromDB = GetAllCostByDateOfPaymentBandFromDB(
            startDate, endDate)
        sumTotal = 0
        for item in searchedCostByBetweenDatesFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Between two dates adds all amount of Cost objects.")
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumCostByDayPerCategory(day, category):
    """Based on the payment date and on the category adds all amount of
    Cost objects.

    Parameters
    ----------
    day : date
        Payment date of Cost objects.
    category : string
        Category of Cost object.

    Returns
    -------
    Integer
        Summarize amount of all Cost objects with the same payment date
        and category from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Cost objects based on the payment date and on the category")
    try:
        searchedCostByDayPerCategoryFromDB = session.query(
            Cost.Cost).filter(Cost.Cost.dateOfPayment == day).filter(
                Cost.Cost.category == category).all()
        sumTotal = 0
        for item in searchedCostByDayPerCategoryFromDB:
            sumTotal += item.amount
        logs.logger.info(
            "Based on the payment date and on the category adds all amount of Cost objects.")
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumCostByMonthPerCategory(year, numberOfMonth, category):
    """Based on the month of payment date and on the category adds all amount of
    Cost objects.

    Parameters
    ----------
    year : integer
        Year of payment date.
    numberOfMonth : integer
        Number of month of payment date.
    category : string
        Category of Cost object.

    Returns
    -------
    Integer
        Summarize amount of all Cost objects with the same month of
        payment date and category from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Cost objects based on the month of payment date and on the category.")
    try:
        num_days = calendar.monthrange(year, numberOfMonth)[1]
        searchedCostByMonthFromDB = GetAllCostByDateOfPaymentBandFromDB(
            date(year, numberOfMonth, 1), date(year, numberOfMonth, num_days))
        sumTotal = 0
        for item in searchedCostByMonthFromDB:
            if item.category.value == category:
                sumTotal += item.amount
        logs.logger.info(
            "Based on the month of payment date and on the category adds all amount of Cost objects.")
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumCostByQuarterPerCategory(year, quarter, category):
    """Based on the quarter of payment date and on the category adds all amount of
    Cost objects.

    Parameters
    ----------
    year : integer
        Year of payment date.
    quarter : integer
        Number of quarter of payment date.
    category : string
        Category of Cost object.

    Returns
    -------
    Integer
        Summarize amount of all Cost objects with the same quarter of
        payment date and category from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Cost objects based on the quarter of payment date and on the category.")
    try:
        first_month_of_quarter = 3 * quarter - 2
        last_month_of_quarter = 3 * quarter
        date_of_first_day_of_quarter = date(year, first_month_of_quarter, 1)
        date_of_last_day_of_quarter = date(
            year, last_month_of_quarter, calendar.monthrange(
                year, last_month_of_quarter)[1])
        searchedCostByQuarterFromDB = GetAllCostByDateOfPaymentBandFromDB(
            date_of_first_day_of_quarter, date_of_last_day_of_quarter)
        sumTotal = 0
        for item in searchedCostByQuarterFromDB:
            if item.category.value == category:
                sumTotal += item.amount
        logs.logger.info(
            "Based on the quarter of payment date and on the category adds all amount of Cost objects.")
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumCostByYearPerCategory(year, category):
    """Based on the year of payment date and on the category adds all amount of
    Cost objects.

    Parameters
    ----------
    year : integer
        Year of payment date.
    category : string
        Category of Cost object.

    Returns
    -------
    Integer
        Summarize amount of all Cost objects with the same year of
        payment date and category from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Cost objects based on the year of payment date and on the category.")
    try:
        first_day_of_year = date(year, 1, 31)
        last_day_of_year = date(year, 12, 31)
        searchedCostByYearFromDB = GetAllCostByDateOfPaymentBandFromDB(
            first_day_of_year, last_day_of_year)
        sumTotal = 0
        for item in searchedCostByYearFromDB:
            if item.category.value == category:
                sumTotal += item.amount
        logs.logger.info(
            "Based on the year of payment date and on the category adds all amount of Cost objects.")
        return sumTotal
    except Exception as e:
        logs.logger.error(e, exc_info=True)


def SumCostByBetweenDatesPerCategory(startDate, endDate, category):
    """Between two payment date and on the category adds all amount of
    Cost objects.

    Parameters
    ----------
    startDate : date
        Start date of payment.
    endDate : date
        End date of payment.
    category : string
        Category of Cost objects.

    Returns
    -------
    Integer
        Summarize amount of all Cost objects between two payment date
        and category from database.
    """

    logs.logger.debug(
        "Start to adds all amount of Cost objects between two payment date and on the category")
    try:
        searchedCostByBetweenDatesFromDB = GetAllCostByDateOfPaymentBandFromDB(
            startDate, endDate)
        sumTotal = 0
        for item in searchedCostByBetweenDatesFromDB:
            if item.category.value == category:
                sumTotal += item.amount
        logs.logger.info(
            "Between two payment date and on the category adds all amount of Cost objects.")
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
        List of Cost objects where the descriptions conain
        the searched string.
    """

    logs.logger.debug(
        "Start to search in description.")
    try:
        NormalizedMySearchedWords = unicodedata.normalize(
            'NFKD', input.upper()).encode('ASCII', 'ignore')
        ListOfAllCost = GetAllCostsFromDB()
        ListOfSearchedCosts = []
        for item in ListOfAllCost:
            NormalizedMyText = unicodedata.normalize(
                'NFKD', item.description.upper()).encode('ASCII', 'ignore')
            if NormalizedMyText.__contains__(NormalizedMySearchedWords):
                ListOfSearchedCosts.append(item)
        logs.logger.info(
            "You search in description")
        return ListOfSearchedCosts
    except Exception as e:
        logs.logger.error(e, exc_info=True)
