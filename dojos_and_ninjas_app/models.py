from django.db import models

class Dojo(models.Model):
    # id is integer field
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default="old dojo")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # Ninja

class Ninja(models.Model):
    # id is integer field
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
