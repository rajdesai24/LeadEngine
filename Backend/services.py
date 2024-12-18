import requests
from django.conf import settings
from rest_framework.response import Response
from .DTOS import LeadDTO
from rest_framework import status
PAGE_ACCESS_TOKEN = "EAAH4c8ZBWmYwBOzYPAQdT4WAzPbq7h2oEQ2hjmYnFxls3z3xlzxiUFmROuSnhQYQc3w9Kwcqwxj3SXQXgHkPtFFl2X9Qmtvhc7Ila0ZCtylPVB9WgxZBcPGhPFpYqyUyNG33LXAdpfLffkNdKljpjXeh3dZBWj7mSwQkJEvRoRfv7ZBtSPoNhm9FXweoZB9FT4JKkjgvDd"

def fetch_lead_data(leadgen_id):
    """
    Fetch lead data from Facebook Graph API using the leadgen_id.
    """
    url = f"https://graph.facebook.com/v21.0/{leadgen_id}"
    headers = {"Authorization": f"Bearer {PAGE_ACCESS_TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error fetching lead data:", response.text)
            return None
    except Exception as e:
        print("Exception:", e)
        return None

def send_lead_to_erpnext(site,lead_data):
    """
    Send lead data to all configured ERPNext sites.
    """
    responses = []
    headers = {
        "Authorization": f"Bearer {site['token']}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(site['url'], json=lead_data, headers=headers)
        if response.status_code == 200:
            responses.append({
                "status": "Success",
                "data": response.json()
            })
        else:
            responses.append({
                "status": "Failed",
                "error": response.text
            })
            return Response({"status":"Failure"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    except Exception as e:
            return Response({"status":"Failure"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)




from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def send_data_to_ERPNext(data):
        try:
            
            # Extract lead details from Facebook payload
            # lead_data = {
            #     "lead_name": "John Doe",  # Replace with data extraction logic
            #     "email_id": "john@example.com",
            #     "phone": "1234567890",
            #     "company_name": "Facebook Lead"
            # }

            # Send lead data to ERPNext sites
            for site in ERP_SITES:
                send_lead_to_erpnext(api_url=site,lead_data=data)

            return Response({
                "status": "Processed",
            }, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


def process_facebook_data(data):

            # Check if the field is 'leadgen' and extract data
            if data.get("field") == "leadgen":
                lead_data = data.get("value", {})
                leadgen_id = lead_data.get("leadgen_id")
                
                if leadgen_id:
                    # Fetch personal lead data from the Graph API

                    personal_data = fetch_lead_data(leadgen_id)
                    send_data_to_ERPNext(personal_data)

def process_99acres_data(data):
 

        # Validate the input data
        # Use the LeadDTO to transform data
        lead_dto = LeadDTO(data)
        transformed_data = lead_dto.transform_acres()
        # Return the transformed data for further use or confirmation
        responses = send_lead_to_erpnext(transformed_data)

        return responses

def process_magicbricks_data(data):
 
    try:
        # Validate the input data
        # Use the LeadDTO to transform data
        lead_dto = LeadDTO(data)
        transformed_data = lead_dto.transform_magicbricks()
        # Return the transformed data for further use or confirmation
        responses = send_lead_to_erpnext(transformed_data)

        return JsonResponse({
                "status": "Processed",
                "details": responses
            }, status=200)
    except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

def process_housing_data(data):
    # Specific processing for Housing.com
 
    try:
        # Validate the input data
        # Use the LeadDTO to transform data
        lead_dto = LeadDTO(data)
        transformed_data = lead_dto.transform_housing()
        # Return the transformed data for further use or confirmation
        responses = send_lead_to_erpnext(transformed_data)

        return JsonResponse({
                "status": "Processed",
                "details": responses
            }, status=200)
    except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

