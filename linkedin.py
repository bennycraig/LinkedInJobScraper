import csv
import fetch
import itertools

# Path to the input and output CSV files	
input_csv_file_path = "input/All SWE Search Terms.csv"
output_csv_file_path = "output/Nov 13 LinkedInScraper Spreadsheet - pass 1.csv"

# Open the CSV file in read mode
with open(input_csv_file_path, 'r') as input_file:
    # Create a CSV reader object
    reader = csv.reader(input_file)

    # Skip the header row if it exists
    header = next(reader, None)

    # Name new columns
    year = "Year"

    # Insert column if it doesn't exist
    if year not in header:
        header.append(year)

    # Get column indices
    year_idx = header.index(year)

    modified_rows = [header] # Create a list to hold the modified rows (which starts with header)

    """ INTERMITTENTLY SAVE THE OUTPUT CSV RESULTS """
    # This prevents crashes from completing deleting all results.
    # Set the interval to write the modified rows to the output CSV file	
    WRITE_INTERVAL = 50	
    processed_lines = 0	


    # Iterate over each row in the CSV input_file
    for i, row in itertools.islice(enumerate(reader, start=0), 10000):

        """ GRAB VALUE FROM SPREADSHEET """
        job_url = row[0] # Extract the URL from the first column (column A)
        print(f"Processing row #{processed_lines}")

        yearResult, salaryResult, employeesResult = fetch.searchUrl(job_url)
        # print(yearResult)
        # print(salaryResult)
        # print(employeesResult)

        """ version 1 - MAKE NEW MODIFIED ROW - INCLUDES ALL ORIGINAL COLUMNS """
        # # Insert yearResult into the Year column
        # row.insert(year_idx, f'"{yearResult}"')  # Insert yearResult within double quotes
        # modified_rows.append(row)  # Append the modified row to the list

        """ version 2 - MAKE NEW MODIFIED ROW - ONLY INCLUDES jobUrl and Year COLUMNS """
        # Create a new row with "jobUrl" and "Year" columns only
        modified_row = [job_url, f'"{yearResult}"']  # Insert yearResult within double quotes
        modified_rows.append(modified_row)  # Append the modified row to the list

        processed_lines += 1

        """ NEW METHOD OF WRITING TO CSV: Intermittently as results are grabbed """
        # Write modified rows to the output CSV file at the specified interval
        if processed_lines % WRITE_INTERVAL == 0:
            with open(output_csv_file_path, 'a', newline='') as output_file:
                # Create a CSV writer object
                writer = csv.writer(output_file)

                # Write the modified rows to the output CSV file
                writer.writerows(modified_rows)

            # Clear the modified_rows list after writing
            modified_rows = []

        # Write any remaining modified rows to the output CSV file
        if modified_rows:
            with open(output_csv_file_path, 'a', newline='') as output_file:
                # Create a CSV writer object
                writer = csv.writer(output_file)

        """"""""""""""""""""" END OF NEW METHOD """""""""""""""""""""


""" ORIGINAL METHOD OF WRITING TO CSV: all at once at end of script (changing for resilience to crashes)"""
# # Write the modified data to the output CSV file
# with open(output_csv_file_path, 'a', newline='') as output_file:
#     # Create a CSV writer object
#     writer = csv.writer(output_file)

#     # Write the modified rows to the output CSV file
#     writer.writerows(modified_rows)

