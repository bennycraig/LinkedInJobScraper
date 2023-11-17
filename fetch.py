"""
MAIN GOALS:
Collect data from any given job posting on...
1. years required
2. salary
3. industry of job (for LinkedIn postings only)
"""

import re
import requests
from bs4 import BeautifulSoup

def findAllMatches(searchTerm, webpage):
    """
    Given a regex pattern and a plain-text webpage, this function returns all matches of that term in a single string separated by " // "
    """
    
    regexPattern = fr"\b" + searchTerm # Construct regex string
    matches = re.finditer(regexPattern, webpage, flags=re.IGNORECASE) # Find all matches
    allMatches = "" # String to store text of all matches
    
    for i, match in enumerate(matches):
        # print("i:", i)
        # print("match:", match)

        # Find start and end of matched word
        start = max(0, match.start() - 2)
        end = min(len(webpage), match.end() + 2)

        # Find the beginning of the preceding word
        if start > 0:
            start_word = webpage.rfind(" ", 0, start) + 1  # the beginning of the preceding word
        else:
            start_word = 0  # the beginning of the text

        # Find the end of the following word
        end_word = webpage.find(" ", end)
        if end_word < 0:
            end_word = len(webpage)
        
        # Get the context (one word before the match, one word after the match)
        context = webpage[start_word:end_word]
        context = context.replace("\n", "") # Remove newlines
        
        # Print debugging
        # print(context) # Full context
        # print(webpage[match.start(): match.end()]) # Only match text
        
        if i == 0:
            allMatches = allMatches + context
        else:
            allMatches = allMatches + " // " + context

    return allMatches


url = "https://www.linkedin.com/jobs/view/3630582123/"

def searchUrl(url):
        
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the HTML content
        html_content = response.text

        # Convert HTML to plain text
        soup = BeautifulSoup(html_content, "html.parser")
        plain_text = soup.get_text()

        # Save the HTML to a file
        with open("job_result.html", 'w') as file:
            file.write(html_content)

        # Save the plain text to a file
        with open("plaintext.txt", 'w') as file:
            file.write(plain_text)

        """ SEARCH FOR YEARS REQUIRED"""

        # Perform regex search for instances of the word "year"
        pattern = fr"\byear"
        pattern = fr"\bsalary"
        # pattern = fr"\bmanager"
        
        yearsResult = findAllMatches("year", plain_text)
        salaryResult = findAllMatches("salary", plain_text)
        employeesResult = findAllMatches("employees ", plain_text)
        
        return (yearsResult, salaryResult, employeesResult)
        
        
        
        
    else:
        print(f"Error: {response.status_code} - Failed to retrieve the HTML content from {url}")
        return ("DEAD LINK", "DEAD LINK", "DEAD LINK")
