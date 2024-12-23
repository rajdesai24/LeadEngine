from django.db import models


class ErrorLog(models.Model):
    """
    Model to log errors for debugging and auditing purposes.
    """

    timestamp = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=255)  # e.g., "ERPNext Site"
    description = models.TextField()  # Detailed error description
    payload = models.JSONField(null=True, blank=True)  # Data that caused the error
