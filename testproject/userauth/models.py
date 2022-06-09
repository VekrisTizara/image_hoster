from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    BASIC = 'BASIC'
    PREMIUM = 'PREMIUM'
    ENTERPRISE = 'ENTERPRISE'
    TIER_CHOICES = [
        (BASIC, 'Basic'),
        (PREMIUM, 'Premium'),
        (ENTERPRISE, 'Enterprise'),
    ]
    tier = models.CharField(choices=TIER_CHOICES, default=BASIC, max_length=10)