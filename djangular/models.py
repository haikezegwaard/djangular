'''
Created on Aug 21, 2015

@author: hz
'''
from django.db import models

class Apple(models.Model):
    color = models.CharField(max_length = 255)
    size = models.IntegerField()
