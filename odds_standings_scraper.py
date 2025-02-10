import requests
from bs4 import BeautifulSoup
import csv
import sys
# Step 1: Install the required libraries
# You can install them using pip:
# pip install requests beautifulsoup4

# Step 2: Fetch the webpage content
url = 'https://www.actionnetwork.com/ncaab/against-the-spread-standings'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url, headers=headers)

# Step 3: Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 4: Extract the desired data
# For example, extracting all the headings
rows = soup.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    if columns:
        data = [column.text.strip() for column in columns]
        print(data)

# Step 5: Save data to CSV
with open('standings.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Team', 'Wins', 'Losses', 'Home_Wins', 'Home_Losses', 'Away_Wins', 'Away_Losses', 'ATS_WINS', 'ATS_Losses', 'ATS_Ties', 'ATS_Home_Wins', 'ATS_Home_Losses','ATS_Home_Ties', 'ATS_Away_Wins', 'ATS_Away_Losses','ATS_Away_Ties', 'OU_Wins', 'OU_Losses','OU_Ties','OU_Home_Wins', 'OU_Home_Losses','OU_Home_Ties', 'OU_Away_Wins', 'OU_Away_Losses','OU_Away_Ties'])  # Write header

    for row in rows:
        columns = row.find_all('td')
        if columns:
            data = [column.text.strip() for column in columns]
            if len(data) >= 9:  # Ensure there are enough columns
                team = data[0]
                #wins/losses
                winloss = data[1].split('-')
                wins = winloss[0]; losses = winloss[1]

                #home wins/losses
                home_winloss = data[2].split('-')
                home_wins = home_winloss[0]; home_losses = home_winloss[1]

                #away wins/losses
                away_winloss = data[3].split('-')
                away_wins = away_winloss[0]; away_losses = away_winloss[1]

                #ATS wins/losses/ties
                ATS_winloss = data[4].split('-')
                ATS_wins = ATS_winloss[0]; ATS_losses = ATS_winloss[1]; 
                
                if len(ATS_winloss) == 3:
                    ATS_ties = ATS_winloss[2]
                else:
                    ATS_ties = 0

                #ATS home wins/losses/ties
                ATS_home_winloss = data[5].split('-')
                ATS_home_wins = ATS_home_winloss[0]; 
                ATS_home_losses = ATS_home_winloss[1]; 
                
                if len(ATS_home_winloss) == 3:
                    ATS_home_ties = ATS_home_winloss[2]
                else:
                    ATS_home_ties = 0     

                #ATS away wins/losses/ties
                ATS_away_winloss = data[6].split('-')
                ATS_away_wins = ATS_away_winloss[0]; ATS_away_losses = ATS_away_winloss[1]; 
                
                if len(ATS_away_winloss) == 3:
                    ATS_away_ties = ATS_away_winloss[2]
                else:
                    ATS_away_ties = 0

                #OU wins/losses/ties
                OU_winloss = data[7].split('-')
                OU_wins = OU_winloss[0]; OU_losses = OU_winloss[1]; 
                    
                if len(OU_winloss) == 3:
                    OU_ties = OU_winloss[2]
                else:
                    OU_ties = 0

                #OU home wins/losses/ties
                OU_home_winloss = data[8].split('-')
                OU_home_wins = OU_home_winloss[0]; OU_home_losses = OU_home_winloss[1]; 
                    
                if len(OU_home_winloss) == 3:
                    OU_home_ties = OU_home_winloss[2]
                else:
                    OU_home_ties = 0

                
                #OU away wins/losses/ties    
                OU_away_winloss = data[9].split('-')
                OU_away_wins = OU_away_winloss[0]; OU_away_losses = OU_away_winloss[1]; 
                
                if len(OU_away_winloss) == 3:
                    OU_away_ties = OU_away_winloss[2]
                else:
                    OU_away_ties = 0
                
                writer.writerow([team] + [wins] + [losses] + [home_wins] + [home_losses] + [away_wins] + [away_losses] + [ATS_wins] + [ATS_losses] + [ATS_ties] + [ATS_home_wins] + [ATS_home_losses] + [ATS_home_ties] + [ATS_away_wins] + [ATS_away_losses] + [ATS_away_ties] + [OU_wins] + [OU_losses] + [OU_ties] + [OU_home_wins] + [OU_home_losses] + [OU_home_ties] + [OU_away_wins] + [OU_away_losses] + [OU_away_ties])\
                
                # Exit the script gracefully
sys.exit()