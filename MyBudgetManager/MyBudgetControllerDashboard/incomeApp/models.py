from django.db import models
from django.db.models import Q, F, Max, Count, Value, Case, When, Sum, ExpressionWrapper, Avg
from django.utils import timezone
from operator import and_, or_, add
from functools import reduce
from django.contrib.auth.models import User, Group
from django.db.models.functions import Concat
from . import validators

from datetime import datetime, timedelta, MAXYEAR
import re
import collections
from money import Money


class IncomeQuerySet(models.QuerySet):
    def all_incomes(self):
        return self.order_by('id')

    def get_the_income_by_id(self, income_id):
        return self.get(income_id=id)

    def create_filters_from_timestamp(self, timestamp):
        dt = datetime.now()
        filters = {}

        try:
            if re.fullmatch(R"([t](oday)?)", timestamp, re.IGNORECASE):
                filters["dateOfPayment__date"] = datetime.today()
            elif re.fullmatch(R"([t](oday)?)\s*-\s*(\d+)", timestamp, re.IGNORECASE):
                days = re.search(R"([t](oday)?)\s*-\s*(\d+)",
                                 timestamp, re.IGNORECASE).group(3)
                end = datetime.today()
                start = end - timedelta(days=int(days))
                filters["dateOfPayment__range"] = (start, end)
            elif re.fullmatch(R"\d{4}[.][01]?\d[.][0-3]?\d\s*-\s*\d{4}[.][01]?\d[.][0-3]?\d", timestamp):
                dtstring = timestamp.split("-")
                start = datetime.strptime(dtstring[0].strip(), "%Y.%m.%d")
                end = datetime.strptime(dtstring[1].strip(), "%Y.%m.%d")
                filters["dateOfPayment__range"] = (start, end)
            elif re.fullmatch(R"\d{4}-[01]?\d-[0-3]?\d\s*-\s*\d{4}-[01]?\d-[0-3]?\d", timestamp):
                dtstring = timestamp.split("-")
                start = datetime.strptime(
                    "".join([x for x in dtstring[0:3]]).strip(), "%Y%m%d")
                end = datetime.strptime(
                    "".join([x for x in dtstring[3:6]]).strip(), "%Y%m%d")
                filters["dateOfPayment__range"] = (start, end)
            elif re.fullmatch(R"\d{4}[.][01]?\d[.][0-3]?\d [0-2]\d:[0-5]\d:[0-5]\d(?:\.\d+)?Z?\s*-\s*\d{4}[.][01]?\d[.][0-3]?\d [0-2]\d:[0-5]\d:[0-5]\d(?:\.\d+)?Z?", timestamp):
                dtstring = timestamp.split("-")
                start = datetime.strptime(
                    dtstring[0].strip(), "%Y.%m.%d %H:%M:%S")
                end = datetime.strptime(
                    dtstring[1].strip(), "%Y.%m.%d %H:%M:%S")
                filters["dateOfPayment__range"] = (start, end)
            elif re.fullmatch(R"\d{4}[.][01]?\d[.][0-3]?\d [0-2]\d:[0-5]\d\s*-\s*\d{4}[.][01]?\d[.][0-3]?\d [0-2]\d:[0-5]\d", timestamp):
                dtstring = timestamp.split("-")
                start = datetime.strptime(
                    dtstring[0].strip(), "%Y.%m.%d %H:%M")
                end = datetime.strptime(dtstring[1].strip(), "%Y.%m.%d %H:%M")
                filters["dateOfPayment__range"] = (start, end)
            elif re.fullmatch(R"[01]?\d[.][0-3]?\d\s*-\s*[01]?\d[.][0-3]?\d", timestamp):
                dtstring = timestamp.split("-")
                start = datetime.strptime(
                    str(dt.year) + "." + dtstring[0].strip(), "%Y.%m.%d")
                end = datetime.strptime(
                    str(dt.year) + "." + dtstring[1].strip(), "%Y.%m.%d")
                filters["dateOfPayment__range"] = (start, end)
            elif re.fullmatch(R"[0-3]?\d\s*-\s*[0-3]?\d", timestamp):
                dtstring = timestamp.split("-")
                start = datetime.strptime(
                    str(dt.year) + "." + str(dt.month) + "." + dtstring[0].strip(), "%Y.%m.%d")
                end = datetime.strptime(
                    str(dt.year) + "." + str(dt.month) + "." + dtstring[1].strip(), "%Y.%m.%d")
                filters["dateOfPayment__range"] = (start, end)
            elif re.fullmatch(R"\d{4}[.-][01]?\d[.-][0-3]?\d [0-2]\d:[0-5]\d:[0-5]\d(?:\.\d+)?Z?", timestamp):
                if "." in timestamp:
                    dt = datetime.strptime(timestamp, "%Y.%m.%d %H:%M:%S")
                if "-" in timestamp:
                    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                filters["dateOfPayment__year"] = dt.year
                filters["dateOfPayment__month"] = dt.month
                filters["dateOfPayment__day"] = dt.day
                filters["dateOfPayment__hour"] = dt.hour
                filters["dateOfPayment__minute"] = dt.minute
                filters["dateOfPayment__second"] = dt.second
            elif re.fullmatch(R"\d{4}[.-][01]?\d[.-][0-3]?\d [0-2]\d:[0-5]\d", timestamp):
                if "." in timestamp:
                    dt = datetime.strptime(timestamp, "%Y.%m.%d %H:%M")
                if "-" in timestamp:
                    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
                filters["dateOfPayment__year"] = dt.year
                filters["dateOfPayment__month"] = dt.month
                filters["dateOfPayment__day"] = dt.day
                filters["dateOfPayment__hour"] = dt.hour
                filters["dateOfPayment__minute"] = dt.minute
            elif re.fullmatch(R"\d{4}[.-][01]?\d[.-][0-3]?\d", timestamp):
                if "." in timestamp:
                    dt = datetime.strptime(timestamp, "%Y.%m.%d")
                if "-" in timestamp:
                    dt = datetime.strptime(timestamp, "%Y-%m-%d")
                filters["dateOfPayment__year"] = dt.year
                filters["dateOfPayment__month"] = dt.month
                filters["dateOfPayment__day"] = dt.day
            elif re.fullmatch(R"[01]?\d[.-][0-3]?\d", timestamp):
                if "." in timestamp:
                    dt = datetime.strptime(timestamp, "%m.%d")
                if "-" in timestamp:
                    dt = datetime.strptime(timestamp, "%m-%d")
                filters["dateOfPayment__month"] = dt.month
                filters["dateOfPayment__day"] = dt.day
            elif re.fullmatch(R"[0-2]\d:[0-5]\d:[0-5]\d(?:\.\d+)?Z?", timestamp):
                dt = datetime.strptime(timestamp, "%H:%M:%S")
                filters["dateOfPayment__hour"] = dt.hour
                filters["dateOfPayment__minute"] = dt.minute
                filters["dateOfPayment__second"] = dt.second
            elif re.fullmatch(R"[0-2]\d:[0-5]\d", timestamp):
                dt = datetime.strptime(timestamp, "%H:%M")
                filters["dateOfPayment__hour"] = dt.hour
                filters["dateOfPayment__minute"] = dt.minute
            elif re.fullmatch(R"[0-3]?\d", timestamp):
                dt = datetime.strptime(timestamp, "%d")
                filters["dateOfPayment__day"] = dt.day
            else:
                filters["dateOfPayment__year"] = MAXYEAR
        except ValueError:
            filters["dateOfPayment__year"] = MAXYEAR

        return filters
    
    def filter_by_timestamp(self, timestamp):
        filters = self.create_filters_from_timestamp(timestamp)
        return self.filter(**filters)
    
    def filter_by_description(self, description):
        filters = description.split(",")
        filters = [f.strip() for f in filters if "" is not f.strip()]
        if not filters:
            filters = [""]
        return self.filter(
            reduce(or_, [Q(description__icontains=description) for description in filters]))
    
    def filter_by_category(self, category):
        filters = category.split(",")
        filters = [f.strip() for f in filters if "" is not f.strip()]
        if not filters:
            filters = [""]
        return self.filter(
            reduce(or_, [Q(category__icontains=category) for category in filters]))


class Incomes(models.Model):
    id = models.AutoField(db_column='id', primary_key=True,
                          null=False, unique=True)
    registrationDate = models.DateTimeField(
        db_column='registrationDate', blank=False, null=False, verbose_name="Registration Date", help_text="e.g. Sept. 12, 2019")
    dateOfPayment = models.DateTimeField(
        db_column='dateOfPayment', blank=False, null=False, verbose_name="Date Of Payment", help_text="e.g. Sept. 12, 2019")
    amount = models.IntegerField(
        db_column='amount', blank=False, null=False, verbose_name="Amount", help_text="e.g. 578 HUF")
    description = models.TextField(db_column='description', blank=False, null=False,
                                   verbose_name="Description", help_text="e.g. Bejovo giro jovairas SP...")
    category = models.CharField(db_column='category', max_length=50, blank=False, null=False,
                                verbose_name="Category", help_text="e.g. Interest Income and Other Revenue From Bank")
    # objects = TestCaseQuerySet.as_manager()

    class Meta:
        managed = False
        db_table = 'incomes'

    def __str__(self):
        return str(self.name)
