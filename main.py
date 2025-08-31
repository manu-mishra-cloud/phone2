from utils import get_recipients, clear_results
from twilio_validator import validate_number 
from result_writer import initialize_results, save_results_batch

BATCH_SIZE = 500  # adjust based on memory/API limits

def main():
    # Clear old results first
    clear_results()

    # Make sure results folder exists
    initialize_results()

    # Load recipients
    recipients = get_recipients()
    print(f"Recipients loaded: {len(recipients)}")

    # Process numbers in batches
    for i in range(0, len(recipients), BATCH_SIZE):
        batch = recipients[i:i + BATCH_SIZE]
        results_batch = []

        for number in batch:
            result = validate_number(number)
            results_batch.append(result)
            print(f"Processed: {number} -> Valid: {result.get('valid')}")

        # Save the batch to files
        save_results_batch(results_batch)
        print(f"Batch {i//BATCH_SIZE + 1} saved.")

if __name__ == "__main__":
    main()
