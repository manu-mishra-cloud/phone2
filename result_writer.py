import os
import json

RESULTS_DIR = "results"
VALID_FILE = os.path.join(RESULTS_DIR, "valid.txt")
INVALID_FILE = os.path.join(RESULTS_DIR, "invalid.txt")
ALL_FILE = os.path.join(RESULTS_DIR, "all.json")


def initialize_results():
    """Prepare results folder and clear previous files."""
    os.makedirs(RESULTS_DIR, exist_ok=True)
    for file_path in [VALID_FILE, INVALID_FILE, ALL_FILE]:
        open(file_path, "w").close()


def save_results_batch(results: list):
    """Save a batch of validation results to files."""
    with open(VALID_FILE, "a") as vf, open(INVALID_FILE, "a") as inf:
        for result in results:
            if result.get("valid"):
                vf.write(f"{result['phone_number']}\n")
            else:
                inf.write(f"{result['phone_number']}\n")

    # Append to all.json
    if os.path.exists(ALL_FILE) and os.path.getsize(ALL_FILE) > 0:
        with open(ALL_FILE, "r+") as f:
            data = json.load(f)
            data.extend(results)
            f.seek(0)
            json.dump(data, f, indent=4)
    else:
        with open(ALL_FILE, "w") as f:
            json.dump(results, f, indent=4)
