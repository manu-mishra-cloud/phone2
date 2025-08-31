from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load Twilio credentials from .env
load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def validate_number(phone_number: str):
    """
    Validate a phone number using Twilio Lookup API
    :param phone_number: E.164 format, e.g., +15551234567
    :return: dict with validation result
    """
    try:
        number_info = client.lookups.v2.phone_numbers(phone_number).fetch(
            type=["carrier"]  # optional: add "caller_name" if needed
        )

        return {
            "phone_number": number_info.phone_number,
            "national_format": number_info.national_format,
            "country_code": number_info.country_code,
            "carrier": number_info.carrier.get("name") if number_info.carrier else None,
            "line_type": number_info.carrier.get("type") if number_info.carrier else None,
            "valid": True,
        }

    except Exception as e:
        # If Twilio cannot validate, mark invalid
        return {
            "phone_number": phone_number,
            "valid": False,
            "error": str(e)
        }
