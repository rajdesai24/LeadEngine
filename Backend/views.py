from .serializers import AcresLeadSerializer,HousingLeadSerializer,MagicBricksLeadSerializer
from django.http import JsonResponse
import json
from .models import Lead
from .services import send_data_to_ERPNext,process_99acres_data,process_magicbricks_data,process_housing_data,process_facebook_data
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import requests
PAGE_ACCESS_TOKEN = "EAAH4c8ZBWmYwBOzYPAQdT4WAzPbq7h2oEQ2hjmYnFxls3z3xlzxiUFmROuSnhQYQc3w9Kwcqwxj3SXQXgHkPtFFl2X9Qmtvhc7Ila0ZCtylPVB9WgxZBcPGhPFpYqyUyNG33LXAdpfLffkNdKljpjXeh3dZBWj7mSwQkJEvRoRfv7ZBtSPoNhm9FXweoZB9FT4JKkjgvDd"

class FacebookLeadsView(generics.GenericAPIView):
    def get(self, request):
        hub_mode = request.GET.get('hub.mode')
        hub_verify_token = request.GET.get('hub.verify_token')
        hub_challenge = request.GET.get('hub.challenge')

        # Replace 'YOUR_VERIFY_TOKEN' with the token you set in Facebook's webhook settings
        if hub_mode == "subscribe" and hub_verify_token == "12345":
            return HttpResponse(hub_challenge, content_type="text/plain")
        return JsonResponse({"error": "Forbidden - Token mismatch"}, status=403)


    def post(self, request):
        try:
            # Process webhook payload
                data = json.loads(request.body)
                result = process_facebook_data(data) 
                return JsonResponse({"status": "Lead processed"}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

class AcresLeadsView(generics.GenericAPIView):
    def post(self, request):
            serializer = AcresLeadSerializer(data=request.data)
            try:
                if serializer.is_valid():
                    # Pass validated data to the processing function
                    validated_data = serializer.validated_data
                    result = process_99acres_data(validated_data) 
                    return Response({"status": "success"}, status=status.HTTP_200_OK)
            except:
                return Response({"status":"Failure"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class MagicBricksLeadsView(generics.GenericAPIView):
    def post(self, request):
        try:
            serializer = MagicBricksLeadSerializer(data=request.data)

            if serializer.is_valid():
                # Pass validated data to the processing function
                validated_data = serializer.validated_data
                result = process_magicbricks_data(validated_data)
                return Response({"status": "success", "result": result}, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

class HousingLeadsView(generics.GenericAPIView):
    def post(self, request):
        try:
            serializer = HousingLeadSerializer(data=request.data)

            if serializer.is_valid():
                # Pass validated data to the processing function
                validated_data = serializer.validated_data
                result = process_housing_data(validated_data)
                return Response({"status": "success", "result": result}, status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
