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

    all_results = []

    # Process numbers in batches
    for i in range(0, len(recipients), BATCH_SIZE):
        batch = recipients[i:i + BATCH_SIZE]
        results_batch = []

        for number in batch:
            result = validate_number(number)
            results_batch.append(result)
            all_results.append(result)
            print(f"Processed: {number} -> Valid: {result.get('valid')}")

        # Save the batch to files
        save_results_batch(results_batch)
        print(f"Batch {i//BATCH_SIZE + 1} saved.")

    # --- Final overview ---
    total = len(all_results)
    valid_numbers = [r for r in all_results if r.get("valid")]
    invalid_numbers = [r for r in all_results if not r.get("valid")]

    # Count line types among valid numbers
    line_types = {}
    for r in valid_numbers:
        lt = r.get("line_type") or "unknown"
        line_types[lt] = line_types.get(lt, 0) + 1

    print("\n--- Validation Summary ---")
    print(f"Total numbers processed: {total}")
    print(f"Valid numbers: {len(valid_numbers)} ({len(valid_numbers)/total*100:.2f}%)")
    print(f"Invalid numbers: {len(invalid_numbers)} ({len(invalid_numbers)/total*100:.2f}%)")

    print("\nLine type breakdown (valid numbers only):")
    for lt, count in line_types.items():
        print(f"  {lt}: {count} ({count/len(valid_numbers)*100:.2f}%)")

if __name__ == "__main__":
    main()
