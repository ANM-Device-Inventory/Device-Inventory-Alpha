from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone

class NIC(models.Model):
    NIC_MAC = models.CharField('MAC ADDR',max_length=100,default="none")
    NIC_TYPE = models.CharField('NIC TYPE',max_length=100,default="none")
    NIC_CAP  = models.CharField('NIC capabilities',max_length=100,default="none")

    def __str__(self):
        return self.NIC_MAC


class HD(models.Model):
    HD_NIC_CPU = models.ForeignKey(NIC,on_delete=models.CASCADE)
    HD_TYPE = models.CharField('HD type',max_length=100,default="none")
    HD_ID = models.CharField('id num', max_length=100,default="none")
    HD_CAP = models.CharField('HD capacity', max_length=100,default="none")

    def __str__(self):
        return self.HD_ID

class CPU(models.Model):
    HD_NIC_CPU = models.ForeignKey(NIC, on_delete=models.CASCADE)
    CPU_TYPE = models.CharField('CPU type',max_length=100,default="none")
    CPU_CORE = models.IntegerField('CPU cores')
    CPU_SPEED = models.FloatField('CPU speed(GB)')

    def __str__(self):
        return self.CPU_TYPE