from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    numberOfPhone = models.CharField(max_length=12)
    card_id = models.BigIntegerField()


class Time_Cafe(models.Model):
    user_id = models.ForeignKey(User)
    #TODO: доделать


class Income(models.Model):
    cafe_id = models.ForeignKey(Time_Cafe)
    sum = models.IntegerField()
    user_id = models.ForeignKey(User)



class Cost(models.Model):


class Card(models.Model):



class Cafe_User(models.Model):