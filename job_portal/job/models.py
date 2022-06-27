from django.db import models
from django.core.validators import RegexValidator

class Applicant(models.Model):
    category=(
        ('Male','male'),
        ('Female','female'),
        ('Other','other'),
    )
    name = models.CharField(max_length=200)
    DOB=models.DateField( auto_now=False, auto_now_add=False)
    gender=models.CharField( max_length=50 ,choices=category)
    resume=models.FileField(upload_to=None, max_length=1000)
    email=models.EmailField( max_length=254)
    phonenumber=models.CharField(max_length=16)

    def __str__(self):
        return self.name
class Recruiter(models.Model):
    company_name=models.CharField( max_length=100)
    company_email=models.EmailField( max_length=254)
    company_phonenumber=models.CharField(max_length=16)
    company_location=models.CharField( max_length=200)

    def __str__(self):
        return self.company_name
    
class Job(models.Model):
    job_title=models.CharField(max_length=50)
    company=models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    description=models.CharField( max_length=1000)
    skills=models.CharField( max_length=500)
    salaryrange=models.IntegerField()
    post_date= models.DateField()
    enddate=models.DateTimeField()
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.job_title
class Application(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    applicant=models.ForeignKey(Applicant() ,on_delete=models.CASCADE)
    applicationdate=models.DateTimeField()
    

    def __str__(self):
        return self.applicant

    def __unicode__(self):
        return 
