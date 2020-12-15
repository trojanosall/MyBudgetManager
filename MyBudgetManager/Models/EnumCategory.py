from enum import Enum

import MyBudgetManager.MyBudgetManager.Log.logs as logs


class EnumCategory(Enum):
    catTvAndInternet = "TV and Internet Service"
    catGasService = "Gas Service"
    catElectricityService = "Electricity Service"
    catWaterSupply = "Water Supply"
    catHeatingService = "Heating Service"
    catGarbageDelivery = "Garbage Delivery"
    catLoanRepayment = "Loan Repayment"
    catGift = "Gift"
    catShopping = "Shopping"
    catElectronicGoods = "Electronic Goods"
    catLili = "Lili"
    catBankCharges = "Bank Charges"
    catTinusLunch = "Tinus Lunch"
    catLociLunch = "Loci Lunch"
    catTraffic = "Traffic"
    catTobacco = "Tobacco"
    catEntertainment = "Entertainment"
    catTinusMobile = "Tinus Mobile"
    catCommonCost = "Common Cost"
    catRentingRelatedCost = "Renting Related Cost"
    catPetrol = "Petrol"
    catHealth = "Health"
    catNPerA = "N/A"
    catLociSalary = "Loci's Salary"
    catTinusSalary = "Tinus's Salary"
    catLociCafeteria = "Loci's Cafeteria"
    catTinusCafeteria = "Tinus's Cafeteria"
    catBankIncomeAndOther = "Interest Income and Other Revenue From Bank"
    catOtherIncome = "Other Income"


def GetListOfEnumCategory():
    """Return the enums of the categories.

    Returns
    -------
    list
        Enum categories.
    """

    logs.logger.debug(
        "Return the enums of the categories.")
    try:
        listOfEnumCategory = []
        for item in EnumCategory:
            listOfEnumCategory.append(item.value)
        return listOfEnumCategory
    except Exception as e:
        logs.logger.error(e, exc_info=True)
