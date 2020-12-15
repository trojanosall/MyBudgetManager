from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType

from MyBudgetManager.MyBudgetManager.Models.base import Base, session
import MyBudgetManager.MyBudgetManager.Models.EnumCategory as EnumCategory


class Cost(Base):

    __tablename__ = "costs"

    id = Column(Integer, primary_key=True)
    registrationDate = Column(Date)
    dateOfPayment = Column(Date)
    amount = Column(Integer)
    description = Column(String)
    category = Column(ChoiceType(EnumCategory.EnumCategory))

    def __init__(self, registrationDate, dateOfPayment, amount, description,
                 category):
        self.registrationDate = registrationDate
        self.dateOfPayment = dateOfPayment
        self.description = description
        self.amount = amount
        self.category = category
