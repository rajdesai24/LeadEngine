import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from lead_engine_logger.db_handler import log_error
import os
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
ERP_SITES = settings.ERP_SITES

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
            raise Exception(detail="There is some issue. Please contact support",code=5000)
    except Exception as e:
        raise Exception(detail="There is some issue. Please contact support",code=5000)
    
def send_lead_to_erpnext(site,lead_data):
    """
    Send lead data to all configured ERPNext sites.
    """
    responses = []
    headers = {
        "Authorization": f"token {site['api_key']}:{site['token']}",
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
            log_error("send_lead_to_erpnext", f"Error sending leads to ERPNext: {str(e)}")
            raise Exception(detail="There is some issue. Please contact support",code=5000)


    except Exception as e:
        log_error("send_lead_to_erpnext", f"Error processing lead: {str(e)}")
        raise Exception(detail="There is some issue. Please contact support",code=5000)


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
                send_lead_to_erpnext(site=site,lead_data=data)

            return Response({
                "status": "Processed",
            }, status=200)
        
        except Exception as e:
            log_error("send_data_to_ERPNext", f"Error processing individual lead: {str(e)}")
            raise Exception(detail="There is some issue. Please contact support",code=5000)


def process_facebook_data(data):

            # Check if the field is 'leadgen' and extract data
            if data.get("field") == "leadgen":
                lead_data = data.get("value", {})
                leadgen_id = lead_data.get("leadgen_id")
                
                if leadgen_id:
                    # Fetch personal lead data from the Graph API

                    personal_data = fetch_lead_data(leadgen_id)
                    send_data_to_ERPNext(personal_data)



