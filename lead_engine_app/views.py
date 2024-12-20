from lead_engine_logger.db_handler import log_error
from .serializers import AcresLeadSerializer,HousingLeadSerializer,MagicBricksLeadSerializer
from django.http import JsonResponse
import json
from .models import Lead
from .services import send_data_to_ERPNext,process_facebook_data
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.exceptions import APIException
from lead_engine_exception_handling.customer_exceptions import GenericException

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
                process_facebook_data(data) 
                return JsonResponse({"status": "Lead processed"}, status=200)

        except Exception as e:
                raise Exception({"status":"Failure"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AcresLeadsView(generics.GenericAPIView):
    
    def post(self, request):
            serializing_data = {
                "lead_name": request.data.get('name'),
                "email_id": request.data.get('email'),
                "phone": request.data.get('phone'),
                "company_name": request.data.get('source'),
            }
            serializer = AcresLeadSerializer(data=serializing_data)
            try:
                if serializer.is_valid():
                    # Pass validated data to the processing function
                    validated_data = serializer.validated_data
                    send_data_to_ERPNext(validated_data) 
                    return Response({"status": "success"}, status=status.HTTP_200_OK)
            except Exception as e:
                log_error("AcresLeadsView", f"Error processing lead: {str(e)}" )
                raise GenericException({"status":"Failure"})
            
class MagicBricksLeadsView(generics.GenericAPIView):
    def post(self, request):
            serializing_data = {
                "lead_name": request.data.get('name'),
                "email_id": request.data.get('email'),
                "phone": request.data.get('phone'),
                "company_name": request.data.get('source'),
            }
            serializer = MagicBricksLeadSerializer(data=serializing_data)
            try:
                if serializer.is_valid():
                    # Pass validated data to the processing function
                    validated_data = serializer.validated_data
                    send_data_to_ERPNext(validated_data) 
                    return Response({"status": "success"}, status=status.HTTP_200_OK)
            except Exception as e:
                log_error("MagicBricksLeadsView", f"Error processing lead: {str(e)}")
                raise GenericException({"status":"Failure"})

class HousingLeadsView(generics.GenericAPIView):
    def post(self, request):
            serializing_data = {
                "lead_name": request.data.get('name'),
                "email_id": request.data.get('email'),
                "phone": request.data.get('phone'),
                "company_name": request.data.get('source'),
            }
            serializer = HousingLeadSerializer(data=serializing_data)
            try:
                if serializer.is_valid():
                    # Pass validated data to the processing function
                    validated_data = serializer.validated_data
                    send_data_to_ERPNext(validated_data) 
                    return Response({"status": "success"}, status=status.HTTP_200_OK)
            except Exception as e:
                log_error("HousingLeadsView", f"Error processing lead: {str(e)}")
                raise GenericException({"status":"Failure"})

