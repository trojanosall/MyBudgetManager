import xml.etree.ElementTree as ET
from datetime import datetime
import MyBudgetManager.MyBudgetManager.Models.Cost as Cost

tree = ET.parse(
    R"C:\Users\troja\Private\Python\MyBudgetManager\MyBudgetManager\FinancialStatementDirectory\convertcsv.xml")
root = tree.getroot()

# print(root[0][0].text)
# print(type(root[0][0].text))
# datetime_object = datetime.strptime("2/1/2019", "%m/%d/%Y").date()
# print(datetime_object)
# print(type(datetime_object))

# for row in root.findall("row"):
#    dateOfPayment = row.find("Konyvelesidatum").text
# description = row.find("Leiras").text
#    amount = int(float((row.find("Osszeg").text).replace(",", ".").replace(" ", "")))
# if "SPAR" in description:
#    print(dateOfPayment, description, amount)
#    print(type(dateOfPayment))
#    print(amount)
#    print(type(amount))

# print(dateOfPayment, description, amount)

# print(float("350.00"))
# print(type(float("350.00")))

Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

Days2 = set(["Tue", "Mon", "Wed", "Thu", "Fri", "Sat", "Sun"])

if Days == Days2:
    print("Egyenló")
else:
    print("nem egyenló")
