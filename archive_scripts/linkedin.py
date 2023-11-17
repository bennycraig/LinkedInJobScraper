import csv
import fetch
import itertools

# Path to the CSV file
# csv_file_path = "result.csv"
csv_file_path = "job_urls_simple.csv"

# Open the CSV file in read mode
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Skip the header row if it exists
    header = next(reader, None)

    # Name new columns
    year = "Year"
    salary = "Salary"
    employees = "Employees"

    # Insert column if it doesn't exist
    if year not in header:
        header.append(year)
    if salary not in header:
        header.append(salary)
    if employees not in header:
        header.append(employees)

    # Get column indices
    year_idx = header.index(year)
    salary_idx = header.index(salary)
    employees_idx = header.index(employees)

    modified_rows = [header] # Create a list to hold the modified rows (which starts with header)

    # Iterate over each row in the CSV file
    # for i, row in enumerate(reader, start=0):
    for i, row in itertools.islice(enumerate(reader, start=0), 100):

        """ GRAB VALUE FROM SPREADSHEET """
        job_url = row[0] # Extract the URL from the first column (column A)
        print(job_url) # Print the URL
        yearResult, salaryResult, employeesResult = fetch.searchUrl(job_url)
        print(yearResult)
        print(salaryResult)
        print(employeesResult)

        """ INSERT VALUE TO SPREADHSEET"""
        # Insert year
        if year_idx < len(row):
            row[year_idx] = yearResult
        else: 
            row.insert(year_idx, yearResult)

        # Insert Salary
        if salary_idx < len(row):
            row[salary_idx] = salaryResult
        else: 
            row.insert(salary_idx, salaryResult)

        # Insert Employees
        if employees_idx < len(row):
            row[employees_idx] = employeesResult
        else: 
            row.insert(employees_idx, employeesResult)

        modified_rows.append(row) # Append the modified row to the list

# Save the modified data back to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the modified rows to the CSV file
    writer.writerows(modified_rows)

