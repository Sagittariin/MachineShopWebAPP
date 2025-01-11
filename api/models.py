from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Orders(models.Model):
    # Choices for plant field
    PLANT_CHOICES = [
        ('AZ', 'Arizona'),
        ('MN', 'Minnesota'),
        ('OH', 'Ohio')
    ]

    # Choices for status field
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_process', 'In Process'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('cancelled', 'Cancelled')
    ]

    part_number = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.PositiveSmallIntegerField(blank=False, null=False, validators=[MinValueValidator(1),MaxValueValidator(99)])
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    plant = models.CharField(max_length=2, choices=PLANT_CHOICES, blank=False, null=False)
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} - {self.part_number}"
