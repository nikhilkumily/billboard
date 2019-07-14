# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Billboard(models.Model):
	billboard_id = models.IntegerField()
	latitude = models.DecimalField(max_digits=30, decimal_places=3)
	longitude = models.DecimalField(max_digits=30, decimal_places=3)
	height = models.DecimalField(max_digits=30, decimal_places=3)
	width = models.DecimalField(max_digits=30, decimal_places=3)
	area_sr = models.DecimalField(max_digits=30, decimal_places=3)
	YES_NO_CHOICES = (
		('Y','Yes'),
		('N', 'No'),
		)
	availablity = models.CharField(max_length=1, choices=YES_NO_CHOICES)
	backlight = models.CharField(max_length=1, choices=YES_NO_CHOICES)

	def __str__(self):
		return str(self.billboard_id) + ' ' + str(self.availablity)