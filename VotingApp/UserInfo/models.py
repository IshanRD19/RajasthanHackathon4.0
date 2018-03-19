from django.db import models

# Create your models here.

class Voter(models.Model):
    ArUcoID = models.CharField(primary_key=True, max_length=2)
    FirstName = models.CharField(max_length=30)
    MiddleName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=30)
    SSN = models.CharField(max_length=12)
    Picture = models.ImageField(upload_to='Voter_Pics/', default='Voter_Pics/None/no_image.jpg')
    DOB = models.DateField(auto_now=False)
    Sex = models.CharField(max_length=12)
    Contact = models.CharField(max_length=12)
    Address = models.CharField(max_length=50)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    Pincode = models.CharField(max_length=6)
    def __str__(self):
        return str(self.ArUcoID)+'-'+(self.FirstName)+' '+str(self.LastName)

class Candidates(models.Model):
    #CandidateID = models.CharField()
    FirstName = models.CharField(max_length=30)
    MiddleName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Picture = models.ImageField(upload_to='Candidate_Pics/', default='Candidate_Pics/None/no_image.jpg')
    Sex = models.CharField(max_length=12)
    DOB = models.DateField(auto_now=False)
    Contact = models.CharField(max_length=12)
    RepresentativeOf = models.CharField(max_length=30)
