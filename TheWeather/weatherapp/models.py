from django.db import models
# Create your models here.

class Weather(models.Model):
	temperature = models.FloatField()
	zipcode = models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	sunrise = models.CharField(max_length=200,default='')
	sunset = models.CharField(max_length=200,default='')
	wind = models.FloatField(default='0')

	def __str__(self):
		return "T:{} Z:{} D:{} S:{} N:{} W:{}".format(self.temperature,self.zipcode,self.description, self.sunrise, self.sunset, self.wind)
