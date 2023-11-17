"""
UPDATE RESULTS
The purpose of this script is to go through and attempt to reload the job URLs of dead links
in the first pass of the program.
"""

import csv
import fetch

# Path to the input and output CSV files
input_csv_file_path = "output/Nov 13 LinkedInScraper Spreadsheet - pass 2.csv"
output_csv_file_path = "output/Nov 13 LinkedInScraper Spreadsheet - pass 3.csv"

# Open the input CSV file in read mode
with open(input_csv_file_path, 'r') as input_file:
    # Create a CSV reader object
    reader = csv.reader(input_file)
    
    # Skip the header row if it exists
    header = next(reader, None)
    
    # Find the index of the "jobId" column
    job_id_idx = header.index("jobId")
    
    modified_rows = []
    dead_link_count = 0
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Get the job URL and current job ID value
        job_url = row[0]
        current_job_id = row[1]
        
        # print(current_job_id)
        # Check if the current job ID value is "DEAD LINK"
        if "DEAD LINK" in current_job_id:

            print("Encountered dead link")

            # Fetch the job URL to see if it's still dead or has new results
            yearResult, _, _ = fetch.searchUrl(job_url)
            
            # Update the job ID value with either "DEAD LINK" or the new results
            if yearResult == "DEAD LINK":
                updated_job_id = "DEAD LINK"
                dead_link_count += 1
            else:
                updated_job_id = yearResult
        else:
            # Keep the current job ID value
            updated_job_id = current_job_id
        
        # Create a new row with the updated job ID
        updated_row = row[:job_id_idx] + [updated_job_id] + row[job_id_idx + 1:]
        modified_rows.append(updated_row)
    
# Write the modified data to the output CSV file
with open(output_csv_file_path, 'w', newline='') as output_file:
    # Create a CSV writer object
    writer = csv.writer(output_file)
    
    # Write the header
    writer.writerow(header)
    
    # Write the modified rows
    writer.writerows(modified_rows)

    # Write the total number of dead links to the cell in the third column, second row
    writer.writerow(["", "", f"Dead Links: {dead_link_count}"])

print(f"Total DEAD LINKs found and updated: {dead_link_count}")
