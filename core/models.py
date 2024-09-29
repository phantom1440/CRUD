from django.db import models

class Info(models.Model):

    f_name = models.CharField(max_length=100, null=False, blank=False)
    l_name = models.CharField(max_length=100, null=False, blank=False)
    m_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)


    def __repr__(self):
        return self.full_name 
    

    