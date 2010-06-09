# -*- coding: utf-8 -*-
from django.db import models

class Publisher(models.Model):
    name     = models.CharField(max_length=20)
    name2    = models.CharField(max_length=20)
    name3    = models.CharField(max_length=20)
    dtbirth  = models.DateField(blank=True)
    city     = models.CharField(max_length=40,blank=True)
    country  = models.CharField(max_length=30,blank=True)
    address  = models.CharField(max_length=60,blank=True)
    website  = models.URLField(blank=True)
    email    = models.EmailField(blank=True)
    

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]