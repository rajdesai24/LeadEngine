from django.db import models

class Lead(models.Model):
    lead_name = models.CharField(max_length=255, default="Unknown")
    email_id = models.EmailField(default="no-email@example.com")
    phone = models.CharField(max_length=20, default="0000000000")
    company_name = models.CharField(max_length=255, default="Unknown Source")
