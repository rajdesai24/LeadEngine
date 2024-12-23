from django.db import models


class Lead(models.Model):
    email_id = models.EmailField(default="no-email@example.com")
    salutation = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    utm_source = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default="New")
    custom_primary_contact_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    custom_secondary_contact_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    whatsapp_no = models.CharField(max_length=20, null=True, blank=True)
    custom_address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    custom_budget = models.IntegerField(null=True, blank=True)
    custom_location_of_property_preferred = models.TextField(null=True, blank=True)
    custom_owner_status = models.CharField(max_length=50, null=True, blank=True)
    custom_requirements = models.TextField(null=True, blank=True)
