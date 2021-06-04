from django.db import models
from django.contrib.auth.models import User
#using pre defined User class to obtain Username , email and password

from phonenumber_field.modelfields import PhoneNumberField


#This model will be used to store values (Name, Phone number, Username, Email ID, Password)
class userProfile(models.Model):
    #Object to store username, email and password
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    

    #To store other details(name and phone number)
    name = models.CharField(max_length=100)
    phoneNumber = PhoneNumberField()

    #using only the username to represent all attributes of a user instance
    def __str__(self):
        return self.user.username