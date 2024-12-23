import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from lead_engine_exception_handling.customer_exceptions import GenericException
from lead_engine_logger.db_handler import log_error
import os
from .serializers import FacebooksLeadSerializer
PAGE_ACCESS_TOKEN = "EAAH4c8ZBWmYwBO5AZBkZAz9OYFMZALZBV7zbrimu9T4igs1XylEqtsfULCLi2x5keIy8ZCteDs2Gd2voCY3hbExBimZAqTfrj24rQLEJacOdVRnQVRk0KZAoUSe0Mb0Xe2Yk0QrY57ldmdEJCZAS7mZCi2s2ZADhjsoiBRmZAHWku3klYDRNiTR5lmt78WNQS528f1ZBpJZAZAJdyKTLjrR9jZAZByJQs3b6wdnkZAPS7K"
ERP_SITES = settings.ERP_SITES


def fetch_lead_data(leadgen_id):
    """
    Fetch lead data from Facebook Graph API using the leadgen_id.
    """
    url = f"https://graph.facebook.com/v21.0/{leadgen_id}"
    headers = {"Authorization": f"Bearer {PAGE_ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.json()
  
    except Exception as e:
        raise GenericException(detail="There is some issue. Please contact support", code=5000)


def send_lead_to_erpnext(site, lead_data):
    """
    Send lead data to all configured ERPNext sites.
    """
    responses = []
    headers = {
        "Authorization": f"token {site['api_key']}:{site['token']}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(site["url"], json=lead_data, headers=headers)
        if response.status_code == 200:
            responses.append({"status": "Success", "data": response.json()})
        else:
            responses.append({"status": "Failed", "error": response.text})

    except Exception as e:
        log_error("send_lead_to_erpnext", f"Error processing lead: {str(e)}")
        raise GenericException(detail="There is some issue. Please contact support", code=5000)


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
            send_lead_to_erpnext(site=site, lead_data=data)

        return Response(
            {
                "status": "Processed",
            },
            status=200,
        )

    except Exception as e:
        log_error("send_data_to_ERPNext", f"Error processing individual lead: {str(e)}")
        raise GenericException(detail="There is some issue. Please contact support", code=5000)


def process_facebook_data(data):

    # Check if the field is 'leadgen' and extract data
        entries = data.get("entry", [])
        for entry in entries:
            changes = entry.get("changes", [])
            for change in changes:
                # Check if the field is 'leadgen'
                if change.get("field") == "leadgen":
                    lead_data = change.get("value", {})
                    leadgen_id = lead_data.get("leadgen_id")
                    
                    if leadgen_id:
                        # Fetch personal lead data from the Graph API
                        personal_data = fetch_lead_data(leadgen_id)
                        serializing_data = {}
                        field_data = personal_data.get('field_data', [])
                        for field in field_data:
                                if field['name'] == 'email':
                                    serializing_data['email_id'] = field['values'][0]
                            
                        # Splitting full_name into parts (if applicable)
                        
                        facebook_serializer = FacebooksLeadSerializer(data=serializing_data)
                        if facebook_serializer.is_valid():
                                # Pass validated data to the processing function
                                validated_data = facebook_serializer.validated_data
                                send_data_to_ERPNext(validated_data)

                        # Send data to ERPNext
