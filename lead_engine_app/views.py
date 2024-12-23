from lead_engine_logger.db_handler import log_error
from .serializers import (
    AcresLeadSerializer,
    HousingLeadSerializer,
    MagicBricksLeadSerializer,
)
from django.http import JsonResponse
import json
from .models import Lead
from .services import send_data_to_ERPNext, process_facebook_data
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.exceptions import APIException
from lead_engine_exception_handling.customer_exceptions import GenericException


class FacebookLeadsView(generics.GenericAPIView):

    def get(self, request):
        hub_mode = request.GET.get("hub.mode")
        hub_verify_token = request.GET.get("hub.verify_token")
        hub_challenge = request.GET.get("hub.challenge")

        # Replace 'YOUR_VERIFY_TOKEN' with the token you set in Facebook's webhook settings
        if hub_mode == "subscribe" and hub_verify_token == "12345":
            return HttpResponse(hub_challenge, content_type="text/plain")
        return JsonResponse({"error": "Forbidden - Token mismatch"}, status=403)

    def post(self, request):
        try:
            # Process webhook payload
            data = json.loads(request.body)
            process_facebook_data(data)
            return JsonResponse({"status": "Lead processed"}, status=200) 

        except Exception as e:
            raise GenericException({"status": "Failure"}, code=4000)


class AcresLeadsView(generics.GenericAPIView):

    def post(self, request):
        serializing_data = {
            "email_id": request.data.get("email"),
            "salutation": request.data.get("salutation"),
            "first_name": request.data.get("first_name"),
            "middle_name": request.data.get("middle_name"),
            "last_name": request.data.get("last_name"),
            "gender": request.data.get("gender"),
            "utm_source": "99 Acres",
            "status": "Lead",
            "custom_primary_contact_number": request.data.get("primary_contact_number"),
            "custom_secondary_contact_number": request.data.get(
                "secondary_contact_number"
            ),
            "whatsapp_no": request.data.get("whatsapp_no"),
            "custom_address_line_1": request.data.get("address_line_1"),
            "custom_address_line_2": request.data.get("address_line_2"),
            "city": request.data.get("city"),
            "state": request.data.get("state"),
            "mobile_no": request.data.get("mobile_no"),
            "country": request.data.get("country"),
            "custom_budget": request.data.get("budget"),
            "custom_location_of_property_preferred_": request.data.get(
                "location_of_property_preferred"
            ),
            "custom_requirements": request.data.get("requirements"),
        }
        serializer = AcresLeadSerializer(data=serializing_data)
        try:

            if serializer.is_valid():
                # Pass validated data to the processing function
                validated_data = serializer.validated_data
                send_data_to_ERPNext(validated_data)
                return Response({"status": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            log_error("AcresLeadsView", f"Error processing lead: {str(e)}")
            raise GenericException({"status": "Failure"}, code=3000)


class MagicBricksLeadsView(generics.GenericAPIView):
    def post(self, request):
        serializing_data = {
            "email_id": request.data.get("email"),
            "salutation": request.data.get("salutation"),
            "first_name": request.data.get("first_name"),
            "middle_name": request.data.get("middle_name"),
            "last_name": request.data.get("last_name"),
            "gender": request.data.get("gender"),
            "utm_source": "Magic Bricks",
            "status": "Lead",
            "custom_primary_contact_number": request.data.get("primary_contact_number"),
            "custom_secondary_contact_number": request.data.get(
                "secondary_contact_number"
            ),
            "whatsapp_no": request.data.get("whatsapp_no"),
            "custom_address_line_1": request.data.get("address_line_1"),
            "custom_address_line_2": request.data.get("address_line_2"),
            "city": request.data.get("city"),
            "state": request.data.get("state"),
            "mobile_no": request.data.get("mobile_no"),
            "country": request.data.get("country"),
            "custom_budget": request.data.get("budget"),
            "custom_location_of_property_preferred_": request.data.get(
                "location_of_property_preferred"
            ),
            "custom_requirements": request.data.get("requirements"),
        }
        serializer = MagicBricksLeadSerializer(data=serializing_data)
        try:

            if serializer.is_valid():
                # Pass validated data to the processing function
                validated_data = serializer.validated_data
                send_data_to_ERPNext(validated_data)
                return Response({"status": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            log_error("AcresLeadsView", f"Error processing lead: {str(e)}")
            raise GenericException({"status": "Failure"}, code=3000)


class HousingLeadsView(generics.GenericAPIView):
    def post(self, request):
        serializing_data = {
            "email_id": request.data.get("email"),
            "salutation": request.data.get("salutation"),
            "first_name": request.data.get("first_name"),
            "middle_name": request.data.get("middle_name"),
            "last_name": request.data.get("last_name"),
            "gender": request.data.get("gender"),
            "utm_source": "Housing.com",
            "status": "Lead",
            "custom_primary_contact_number": request.data.get("primary_contact_number"),
            "custom_secondary_contact_number": request.data.get(
                "secondary_contact_number"
            ),
            "whatsapp_no": request.data.get("whatsapp_no"),
            "custom_address_line_1": request.data.get("address_line_1"),
            "custom_address_line_2": request.data.get("address_line_2"),
            "city": request.data.get("city"),
            "state": request.data.get("state"),
            "mobile_no": request.data.get("mobile_no"),
            "country": request.data.get("country"),
            "custom_budget": request.data.get("budget"),
            "custom_location_of_property_preferred_": request.data.get(
                "location_of_property_preferred"
            ),
            "custom_requirements": request.data.get("requirements"),
        }
        serializer = HousingLeadSerializer(data=serializing_data)
        try:

            if serializer.is_valid():
                # Pass validated data to the processing function
                validated_data = serializer.validated_data
                send_data_to_ERPNext(validated_data)
                return Response({"status": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            log_error("AcresLeadsView", f"Error processing lead: {str(e)}")
            raise GenericException({"status": "Failure"}, code=3000)
