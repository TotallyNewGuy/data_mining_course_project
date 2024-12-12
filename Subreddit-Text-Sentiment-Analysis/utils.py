import csv
import pandas as pd
import os

def save_results_to_csv(results, output_file):
    processed_results = []
    for result in results:
        for post_id, data in result.items():  # Unpack the single key-value pair
            processed_results.append({'post_id': post_id, 'result': data})

    # Convert to a DataFrame
    df = pd.DataFrame(processed_results)

    # Save to CSV (append or create new file)
    if not os.path.exists(output_file):
        df.to_csv(output_file, index=False)
    else:
        df.to_csv(output_file, mode='a', header=False, index=False)

def validate_result(result):
    # Placeholder for validation logic
    return result and result.get('result') is not None
