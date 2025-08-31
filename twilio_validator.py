from twilio.rest import Client
from dotenv import load_dotenv
import random
import os

load_dotenv()

# Some mock carriers and line types
CARRIERS = ["Verizon", "AT&T", "T-Mobile", "Sprint", "Vodafone", "MockCarrier"]
LINE_TYPES = ["mobile", "landline", "voip"]

def validate_number(phone_number: str):
    """
    Realistic mock function to simulate Twilio Lookup API
    """
    # Randomly decide if the number is valid (70% chance valid)
    is_valid = random.choices([True, False], weights=[70, 30])[0]

    if is_valid:
        return {
            "phone_number": phone_number,
            "national_format": f"({phone_number[2:5]}) {phone_number[5:8]}-{phone_number[8:]}",
            "country_code": phone_number[1:3],  # crude mock
            "carrier": random.choice(CARRIERS),
            "line_type": random.choice(LINE_TYPES),
            "valid": True,
        }
    else:
        return {
            "phone_number": phone_number,
            "valid": False,
            "error": "Invalid number (mock)"
        }