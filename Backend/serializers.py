from rest_framework import serializers

class AcresLeadSerializer(serializers.Serializer):
    """
    Serializer for 99 Acres lead data.
    """
    name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(max_length=15, required=True)
    source = serializers.CharField(max_length=50, required=True)
    message = serializers.CharField(max_length=500, required=False, allow_blank=True)
    property_id = serializers.CharField(max_length=50, required=False, allow_blank=True)
    query_date = serializers.DateTimeField(required=False, allow_null=True)

class MagicBricksLeadSerializer(serializers.Serializer):
    """
    Serializer for 99 Acres lead data.
    """
    name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(max_length=15, required=True)
    source = serializers.CharField(max_length=50, required=True)
    message = serializers.CharField(max_length=500, required=False, allow_blank=True)
    property_id = serializers.CharField(max_length=50, required=False, allow_blank=True)
    query_date = serializers.DateTimeField(required=False, allow_null=True)

class HousingLeadSerializer(serializers.Serializer):
    """
    Serializer for 99 Acres lead data.
    """
    name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(max_length=15, required=True)
    source = serializers.CharField(max_length=50, required=True)
    message = serializers.CharField(max_length=500, required=False, allow_blank=True)
    property_id = serializers.CharField(max_length=50, required=False, allow_blank=True)
    query_date = serializers.DateTimeField(required=False, allow_null=True)

