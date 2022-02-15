######################################################################################
# Visit Centennial College Artificial Intelligence program webpage.
# Write a code that can fetch and printout following information
# a. The title of the website
# b. All possible companies offering jobs under the "Companies Offering Jobs" heading
# c. All possible careers under "Career Outlook" heading
# Export the fetched information into a file

import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import ssl

# constant
DIR_OUTPUT = os.getcwd()
CSV_FILENAME = 'program_info.csv'
URL = 'https://www.centennialcollege.ca/programs-courses/full-time/artificial-intelligence-online/'

# get html and sopified instance
context = ssl._create_unverified_context()
html = urlopen(URL, context=context).read()
soup = BeautifulSoup(html, "html.parser")

# get title of the website
title = soup.find("title").get_text()
print(f'1. Title of the website: \n{title}\n')

# all possible companies offering jobs
p_companies = soup.find("h3", text='Companies Offering Jobs').next_sibling.next_sibling
companies = p_companies.get_text()
print(f'2. Companies offering jobs: \n{companies}\n')

# all possible careers
ul_careers = soup.find("h3", text='Career Outlook').next_sibling.next_sibling
careers_lst = [li_company.get_text() for li_company in ul_careers.contents if li_company.get_text() != '\n']
careers = ", ".join(careers_lst)
print(f'3. All possible careers: \n{careers}')

# write csv
with open(os.path.join(DIR_OUTPUT, CSV_FILENAME), 'w') as f:
    writer = csv.writer(f , lineterminator='\n')
    writer.writerow(('title', 'companies offering', 'possible careers'))
    writer.writerow((title, companies, careers))