from django.db import models

# Create your models here.
class Skill(models.Model):
    description = models.TextField(max_length=250)
    skill_level = models.IntegerField()

    def __str__(self):
        return self.name