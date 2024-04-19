from django.db import models

class User(models.Model):
    fullname=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    course=models.CharField(max_length=255)
    city=models.CharField(max_length=255)

    def __str__(self):
        return self.fullname +' ' + str(self.email)

