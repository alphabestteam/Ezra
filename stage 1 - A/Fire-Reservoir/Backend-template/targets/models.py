from django.db import models

class Target(models.Model):
    # Implement here a target model with a __str__ function
    # how the db looks
    name = models.CharField(max_length=100)
    attack_priority = models.IntegerField()
    longitude = models.DecimalField(decimal_places=3, max_digits=5)
    latitude = models.DecimalField(decimal_places=3, max_digits=5)
    enemy_organization = models.CharField(max_length=100)
    target_goal = models.CharField(max_length=100)
    was_target_destroyed = models.BooleanField(null=True)
    target_id = models.IntegerField(unique=True)

    