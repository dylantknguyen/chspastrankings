# FIRST Chesapeake Past Rankings
This file finds the average ranking of all CHS teams during certain years using The Blue Alliance API. It outputs the data to a spreadsheet.

## Generating and Adding an Access Token
In order to make calls to the The Blue Alliance API, you must generate your own token. To do this, go to your TBA Account Dashboard. Next, scroll down to the `Read API Keys` section, enter a description into the description box, and click "Add New Key". 

After generating your key, go back to the code and find the line with `'X-TBA-Auth-Key': ''`. Add your key between the second pair of quotations so that it looks like `'X-TBA-Auth-Key': '[Your Token]'` with [Your Token] being the token you generated above. Now, you're set to start using The Blue Alliance API!

## Running Program
To install the program, just download the repo using the "Clone or Download" button. It is likely that you will need to install the python package `openpyxl` using the command `pip install openpyxl` in your command line interface.  Once you do that, just double click `teamranking.py`. It should create an Excel spreadsheet in the same folder. Open it and check out the numbers.

Note: This requires Python to work.
## Changing Years
To run, change the years array to the desired years. Make sure to put the year in single quotations

### Example
```
years = ['2016', '2017', '2018', '2019']
```
This would have the program find the average rankings of all Chesapeake teams during the years 2016, 2017, 2018, 2019.

## Printing to Excel Spreadsheet
While you can add the data to an excel spreadsheet, you can also just have it print out the rankings. To do this, comment out the following lines:
```
workbook = openpyxl.Workbook()
sheet = workbook.active

sheet["A1"] = "Team"
sheet["B1"] = "Average Ranking" 
```
and 
```
workbook.save(filename="Chesapeake Past Team Rankings.xlsx")
```
Then, replace `sheet.append(teamrank)` with print(teamrank). 
