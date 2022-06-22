from django.db import models
from django.utils import timezone

class PersonelDataBase(models.Model):
	#id = models.BigAutoField(primary_key = True)
	personelid=models.IntegerField()
	tckn=models.IntegerField()
	name= models.CharField(max_length=25, blank=False, null=False)
	surname= models.CharField(max_length=25, blank=False, null=False)
	sgk=models.IntegerField()
	bloodtype= models.CharField(max_length=25, blank=False, null=False)
	fathername= models.CharField(max_length=25, blank=False, null=False)
	mothername= models.CharField(max_length=25, blank=False, null=False)
	status= models.CharField(max_length=25, blank=False, null=False)
	birthplace= models.CharField(max_length=25, blank=False, null=False)
	birthdate= models.CharField(max_length=25, blank=False, null=False)
	province= models.CharField(max_length=25, blank=False, null=False)
	militarystatus= models.CharField(max_length=25, blank=False, null=False)
	school= models.CharField(max_length=25, blank=False, null=False)
	department= models.CharField(max_length=25, blank=False, null=False)
	telephone=models.IntegerField()
	email= models.EmailField()
	address= models.TextField(blank=True)
	def __str__(self):
		return self.name