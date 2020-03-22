import requests
import openpyxl

""" Import Data from Past Years """
# urls
years = ['2016', '2017', '2018', '2019']
links = {}
for year in years:
    links[year] = str('https://www.thebluealliance.com/api/v3/district/' + year + 'chs/rankings')

# header with token
headers = {
    'X-TBA-Auth-Key': ''
}

""" Get Requests """
# rankings from past 4 years
rankings = {}
for year in links:
    rankings[year] = requests.get(links[year], headers=headers).json()

# current teams list
teamslist = 'https://www.thebluealliance.com/api/v3/district/2020chs/teams'
teams20 = requests.get(teamslist, headers=headers).json()

""" Creates Spreadsheet """
workbook = openpyxl.Workbook()
sheet = workbook.active

sheet["A1"] = "Team"
sheet["B1"] = "Average Ranking"

# finds team in rankings and averages past rankings
for currentteam in teams20:
    teamrank = []
    ranks = []
    teamnumber = currentteam['team_number']
    teamrank.append(teamnumber)
    teamkey = currentteam['key']
    for year in years:
        yearanalyzing = rankings[year]
        for teams in yearanalyzing:
            if teamkey == teams['team_key']:
                ranks.append(teams['rank'])
    if len(ranks) != 0:
        rankingavg = sum(ranks) / len(ranks)
        teamrank.append(rankingavg)
        sheet.append(teamrank)

workbook.save(filename="Chesapeake Past Team Rankings.xlsx")
