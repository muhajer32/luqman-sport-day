from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Participant(models.Model):
    AGE_GROUPS = [
        ('U12', 'Under 12'),
        ('U15', 'Under 15'),
        ('U18', 'Under 18'),
        ('O18', 'Over 18'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age_group = models.CharField(max_length=3, choices=AGE_GROUPS)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    activities = models.ManyToManyField('Activity', related_name='participants')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.age_group}) - {self.gender}"
    
