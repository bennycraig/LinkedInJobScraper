import csv
import fetch

# Path to the CSV file
csv_file_path = "result.csv"

# Open the CSV file in read mode
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Skip the header row if it exists
    header = next(reader, None)

    # INSERT COLUMN: Find the index of the "Test" column or add it if it doesn't exist
    new_column = "Test"
    if new_column in header:
        column_index = header.index(new_column)
    else: 
        header.append(new_column)
        column_index = header.index(new_column)

    print(header.index(new_column))
    print(len(header))
    # column_index = header.index(new_column) if new_column in header else len(header)

    # # Add new column to header if it doesn't exist
    # if column_index == len(header):
    #     header.append(new_column)

    modified_rows = [header] # Create a list to hold the modified rows (which starts with header)

    # Iterate over each row in the CSV file
    for i, row in enumerate(reader, start=0):

        """ GRAB VALUE FROM SPREADSHEET """
        job_url = row[0] # Extract the URL from the first column (column A)
        # print(job_url) # Print the URL
        # yearsResult, salaryResult, employeesResult = fetch.searchUrl(job_url)

        """ INSERT VALUE TO SPREADHSEET"""
        if column_index < len(row):
            row[column_index] = str(i)
        else: 
            row.insert(column_index, str(i)) # Insert the incrementing number in the "Test" column
        modified_rows.append(row) # Append the modified row to the list

# Save the modified data back to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the modified rows to the CSV file
    writer.writerows(modified_rows)


""" 
CODE TO DELETE A COLUMN
Place this immediately after the line of code that finds the column index of the column to delete

    # If the column exists, delete it from the header and rows
    if column_index is not None:
        header.pop(column_index)
        rows = [row[:column_index] + row[column_index+1:] for row in reader]
    else:
        rows = list(reader)

    # Save the modified data back to the CSV file
    with open(csv_file_path, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the header and modified rows to the CSV file
        writer.writerow(header)
        writer.writerows(rows)
 """