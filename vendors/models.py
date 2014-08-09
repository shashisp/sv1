from django.db import models
from autoslug.fields import AutoSlugField
# Create your models here.



class Organisation(models.Model):
		CITY_CHOICES = (
           ('1', 'Dharwad'),
           ('2', 'Hubli'),
           ('3', 'Pune'),
           ('4', 'Belgaum'),
           ('5', 'Others'),
         )
		SERVICE_CHOICES = (
			('1', 'Photography'),
			('2', 'Caterers'),
			('3', 'Cakeshops'),
			('4', 'Decorators'),
			('5', 'Venues'),
			('6', 'Printing Service'),
			('7', 'Others')
			)
		name = models.CharField('Organisation Name',max_length=200)
		service_type = models.CharField("Service Type", max_length=200, choices=SERVICE_CHOICES)
		address = models.TextField(max_length=500)
		city = models.CharField('City', max_length=200, choices=CITY_CHOICES)
		contact = models.CharField('Phone', max_length=10,blank=False)
		slug = AutoSlugField(populate_from=('name'))
		logo = models.URLField("Enter Logo URL",blank=False)
		description = models.TextField(blank=True)
		#logo = models.ImageField()


		def __unicode__(self):
				return self.name
