from rest_framework import serializers
from .models import Lead
class AcresLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ["lead_name", "email_id", "phone", "company_name"]

class MagicBricksLeadSerializer(serializers.Serializer):
    """
    Serializer for 99 Acres lead data.
    """
    class Meta:
        model = Lead
        fields = ["lead_name", "email_id", "phone", "company_name"]


class HousingLeadSerializer(serializers.Serializer):
    """
    Serializer for 99 Acres lead data.
    """
    class Meta:
        model = Lead
        fields = ["lead_name", "email_id", "phone", "company_name"]

