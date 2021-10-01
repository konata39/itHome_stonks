from django.db import models

# Create your models here.
class stonks_DB(models.Model):
    comp_id = models.IntegerField() #公司代號
    year = models.IntegerField() #財報年度
    season = models.IntegerField() #財報季度
    balance_sheet = models.CharField(max_length = 10000) #負債表
    income_statement = models.CharField(max_length = 10000) #損益表
