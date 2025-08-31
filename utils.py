import os
import phonenumbers



def get_recipients(file_path="recipient.txt", default_region="US"):
   
    recipients = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                raw_number = line.strip()
                if not raw_number:
                    continue

                try:
                    number_obj = phonenumbers.parse(raw_number, default_region)
                    if phonenumbers.is_valid_number(number_obj):
                        formatted = phonenumbers.format_number(
                            number_obj, phonenumbers.PhoneNumberFormat.E164
                        )
                        recipients.append(formatted)
                except phonenumbers.NumberParseException:
                    # skip silently
                    pass
    except FileNotFoundError:
        # if file missing, just return empty list
        return []

    return recipients



# Paths to results
RESULTS_DIR = "results"
VALID_FILE = os.path.join(RESULTS_DIR, "valid.txt")
INVALID_FILE = os.path.join(RESULTS_DIR, "invalid.txt")
MOBILE_FILE = os.path.join(RESULTS_DIR, "mobile.txt")
LANDLINE_FILE = os.path.join(RESULTS_DIR, "landline.txt")
ALL_FILE = os.path.join(RESULTS_DIR, "all.json")


def clear_results():
    """Clear previous result files before starting a new run."""
    os.makedirs(RESULTS_DIR, exist_ok=True)  # make sure folder exists

    # Clear each file
    for file_path in [VALID_FILE, INVALID_FILE, MOBILE_FILE, LANDLINE_FILE, ALL_FILE]:
        open(file_path, "w").close()