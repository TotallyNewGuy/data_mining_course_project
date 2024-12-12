import csv
import psycopg2
from tqdm import tqdm

# Database configuration
db_config = {
    "dbname": "",
    "user": "",
    "password": "",
    "host": "",
    "port": ,
}

# Define the file path (replace this with your actual CSV file path)
csv_file_path = "data/first_10-out.csv"  # Replace with the path to your uploaded file

# Function to import CSV into PostgreSQL
def import_csv_to_postgresql(file_path, table_name, db_config):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Open the CSV file to calculate the total number of rows
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            total_rows = sum(1 for _ in csv_file) - 1  # Subtract 1 for the header row

        # Open the CSV file again for actual processing
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row

            # Wrap the reader with tqdm for progress display
            for row in tqdm(reader, total=total_rows, desc="Importing rows"):
                post_id = row[0].strip()
                result = row[1].strip()
                cursor.execute(
                    f"INSERT INTO {table_name} (post_id, result) VALUES (%s, %s)",
                    (post_id, result),
                )

        # Commit the transaction
        conn.commit()

        print(f"Data from {file_path} successfully imported into {table_name}.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Call the function
import_csv_to_postgresql(csv_file_path, "sentiment_copy1", db_config)
