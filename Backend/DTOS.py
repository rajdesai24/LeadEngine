class LeadDTO:
    """
    Data Transfer Object for transforming lead data into the ERPNext format.
    """
    def __init__(self, raw_data):
        self.raw_data = raw_data
    def transform_facebook(self):
        try:

            # Extract fields from the Facebook response
            field_data = {field["name"]: field["values"][0] for field in self.raw_data.get("field_data", [])}

            # Map Facebook fields to ERPNext format
            return {
                "lead_name": field_data.get("full_name", "Unknown"),
                "email_id": field_data.get("email", "no-email@example.com"),
                "phone": field_data.get("phone_number", "0000000000"),
                "company_name": "Facebook Lead"  # Static value for Facebook leads
            }
        except Exception as e:
            raise ValueError(f"Error transforming Facebook data: {str(e)}")

    def transform_acres(self):
        """
        Transforms raw lead data into the required ERPNext format.

        Returns:
            dict: Transformed lead data.
        """
        try:
            return {
                "lead_name": self.raw_data.get("name", "Unknown"),  # Replace with actual field mapping
                "email_id": self.raw_data.get("email", "no-email@example.com"),
                "phone": self.raw_data.get("phone", "0000000000"),
                "company_name": self.raw_data.get("source", "Unknown Source")
            }
        except Exception as e:
            raise ValueError(f"Error transforming data: {str(e)}")
        
    def transform_housing(self):
        """
        Transforms raw lead data into the required ERPNext format.

        Returns:
            dict: Transformed lead data.
        """
        try:
            return {
                "lead_name": self.raw_data.get("name", "Unknown"),  # Replace with actual field mapping
                "email_id": self.raw_data.get("email", "no-email@example.com"),
                "phone": self.raw_data.get("phone", "0000000000"),
                "company_name": self.raw_data.get("source", "Unknown Source")
            }
        except Exception as e:
            raise ValueError(f"Error transforming data: {str(e)}")
        
    def transform_magicbricks(self):
        """
        Transforms raw lead data into the required ERPNext format.

        Returns:
            dict: Transformed lead data.
        """
        try:
            return {
                "lead_name": self.raw_data.get("name", "Unknown"),  # Replace with actual field mapping
                "email_id": self.raw_data.get("email", "no-email@example.com"),
                "phone": self.raw_data.get("phone", "0000000000"),
                "company_name": self.raw_data.get("source", "Unknown Source")
            }
        except Exception as e:
            raise ValueError(f"Error transforming data: {str(e)}")
