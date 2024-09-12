from django.db import models

# Create your models here.
# models.py

class Customer:
    def __init__(self, id, name, phone_number):
        self.id = id
        self.name = name
        self.phone_number = phone_number
