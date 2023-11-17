# Entry Level LinkedIn Scraper 🚀

A common issue when looking for entry-level roles on LinkedIn is that even jobs marked as "Entry Level" on LinkedIn often require 3, 4, 5, or more years of experience. I wrote this **Python scraping tool to automatically search job descriptions** so I can rule out **which jobs are entry-level and which are definitely not**.

This program gathers information about job postings by scraping a list of URLs. For each posting, the script performs a word search for any instance of the word "years" to find out how many years are required for that job. The result is appended to a spreadsheet for easy filtering and sorting.

This Google Sheet shows an example of the end result: https://docs.google.com/spreadsheets/d/10PAGF_Sk1rSO-l6MxFMof6L9TIdVddewaujgGsFyYkw/edit?usp=sharing

![Entry Level Tech Roles Spreadsheet](img/Entry%20Level%20Tech%20Roles.png)

# Getting Started

To run this script locally using your own spreadsheet of job links:

1. Clone the repo

```sh
git clone https://github.com/bennycraig/LinkedInJobScraper.git
```

2. Modify the input CSV file and output CSV file

    - Add your CSV spreadsheet of Job URLs to the input folder
    - In linkedin.py, change the values for `input_csv_file_path` and `output_csv_file_path` on lines 6 and 7.
    

3. Run the linkedin.py 
```sh
python linkedin.py
```

