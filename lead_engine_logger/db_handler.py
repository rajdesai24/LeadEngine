from .models import ErrorLog


def log_error(source, description, payload=None):

    ErrorLog.objects.create(source=source, description=description, payload=payload)
