from django.db import models
from django_autoslug.fields import AutoSlugField




class Contact(models.Model):
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
	name = models.CharField(max_length=100)
	service_type = models.CharField("Service Type", max_length=200, choices=SERVICE_CHOICES)
	name = models.CharField('Organisation Name',max_length=200)
	phone = models.IntegerField()
	email = models.EmailField()
	logo = models.URLField("Enter Logo URL",blank=False)
	address = models.TextField()
	timings = models.TextField("Enter Timings")
	description = models.TextField(blank=True)
	slug = AutoSlugField(populate_from='name')

	def __unicode__(self):
		return self.name


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
		logo = models.URLField("Enter Logo URL",blank=False)
		description = models.TextField(blank=True)
		slug = AutoSlugField(populate_from=('name'))
		
		#logo = models.ImageField()


		def __unicode__(self):
				return self.name