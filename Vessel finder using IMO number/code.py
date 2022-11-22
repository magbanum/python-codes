"""
Project name: Vessel finder using IMO number
Description: This code collects the IMO numbers from the excel and search the Vessels assigned to it. Then it creates new sheet in same excel and save the results there.
Dependencies: Pandas, Requests, BeautifulSoap, Openpyxl
Author: Shantanu Nighot
"""

import pandas as pd
import requests
from types import NoneType
from bs4 import BeautifulSoup
from openpyxl import load_workbook

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

# Read content of vessels.xlsx into data
data = pd.read_excel(r'vessels.xlsx') 
df = pd.DataFrame(data)
# Fill empty cells with 0
df['IMO'] = df['IMO'].fillna(0).astype(int)


vessel_list = []
counter = 0

# Loop through the IMO numbers
print("Vessels search started....")
for item in df.values:
    # URL to get vessel name from IMO number
    url = "https://www.vesselfinder.com/vessels?name={IMO}".format(IMO=str(item[0]))
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    # Find the div with class as slna in html
    results = soup.find("div", {"class": "slna"})
    # If result is not NoneType i.e. found vessel on IMO number then append to vessel_list
    # Else append "Not found".
    if(type(results) != NoneType):
        vessel_list.append(results.text)
    else:
        vessel_list.append("Not found")

    # Notify after every 1000 vessels completed
    counter += 1
    if (counter % 1000 == 0 and counter > 1000):
        print("Completed " + str(counter) + " Vessels")

# Add the collected vessel names list to Dataframe
df['Vessel name'] = pd.DataFrame(vessel_list)
# Load the vessel.xlsx
ExcelWorkbook = load_workbook('vessels.xlsx')
writer = pd.ExcelWriter('vessels.xlsx', engine = 'openpyxl')
writer.book = ExcelWorkbook
# Add Dataframe to the new sheet of selected excel
df.to_excel(writer, sheet_name = 'Result')
# Save and cole the Excelwriter
writer.save()
writer.close()
print("Vessels search completed and saved in vessels.xlsx")