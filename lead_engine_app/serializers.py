from rest_framework import serializers
from .models import Lead


class AcresLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"


class MagicBricksLeadSerializer(serializers.ModelSerializer):
    """
    Serializer for 99 Acres lead data.
    """

    class Meta:
        model = Lead
        fields = "__all__"


class HousingLeadSerializer(serializers.ModelSerializer):
    """
    Serializer for 99 Acres lead data.
    """

    class Meta:
        model = Lead
        fields = "__all__"


class FacebooksLeadSerializer(serializers.ModelSerializer):
    """
    Serializer for 99 Acres lead data.
    """

    class Meta:
        model = Lead
        fields = ["email_id", "first_name", "last_name","last_name"]
