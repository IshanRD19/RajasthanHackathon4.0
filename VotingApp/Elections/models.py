from django.db import models

# Create your models here.

class Elections(models.Model):
    ElectionID = models.CharField(primary_key=True, max_length=10)
    AssociatedWith = models.CharField(max_length=50)
    FromDate = models.DateField(auto_now=False)
    EndDate = models.DateField(auto_now=False)
    def __str__(self):
        return str(self.ElectionID)+'-'+str(self.AssociatedWith)





