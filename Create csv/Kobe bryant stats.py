import requests
from bs4 import BeautifulSoup as bs
import re
from csv import writer

class Kobe():

    """CLASS THAT RETURNS A CSV WITH THE STATS FOR KOBE BRYANT'S CAREER"""

    def __init__(self):
        self.name = "Kobe Bryant"
        self.url = "https://www.basketball-reference.com/players/b/bryanko01/gamelog/"


    def season_stats(self, url):

        """FUNCTION THAT SCRAPES DATA FROM ONE SEASON
         AND RETURNS A LIST OF TUPLES"""

        page = requests.get(url)
        soup = bs(page.text, "html.parser")


        titles = soup.find_all('h2')
        current_season = titles[1].text.split(" ")[0]


        # FIND REGULAR SEASON TABLE
        table = soup.find(id="pgl_basic")

        #FIND ALL ROWS
        table_row = table.find_all("tr")


        stats = []
        for row in table_row[1:]:

            if "thead" not in str(row):
                date_game = row.find("a").text
                age = str(row).split('data-stat="age">')[1].split("<")[0]
                game_result = str(row).split('data-stat="game_result">')[1].split("<")[0]
                opponent = str(row).split('data-stat="opp_id">')[1].split("teams/")[1].split("/")[0]

            try:
                points = str(row).split('data-stat="pts">')[1].split("<")[0]
                asists = str(row).split('data-stat="ast">')[1].split("<")[0]
                rebounds = str(row).split('data-stat="trb">')[1].split("<")[0]
                turnovers = str(row).split('data-stat="tov">')[1].split("<")[0]
                steals = str(row).split('data-stat="stl">')[1].split("<")[0]
                blocks = str(row).split('data-stat="blk">')[1].split("<")[0]
                minutes_played = str(row).split('data-stat="mp">')[1].split("<")[0]
                fg_pct = str(row).split('data-stat="fg_pct">')[1].split("<")[0]
                fg3_pct = str(row).split('data-stat="fg3_pct">')[1].split("<")[0]
                ft_pct = str(row).split('data-stat="ft_pct">')[1].split("<")[0]
            except:
                asists = points = rebounds = turnovers = blocks = ""
                minutes_played = steals = fg_pct = fg3_pct = ""
                ft_pct = "Did not play"

            stats.append((date_game,age,game_result,opponent,points,asists,rebounds,turnovers,steals,blocks,minutes_played,
                          fg_pct,fg3_pct,ft_pct,current_season))


        return stats


    def season_link(self):

        """GENERATE A LIST WITH THE LINKS FOR ALL SEASONS
         AND FOR EVERY SEASON IT GRABS ALL STATS. RETURNS STATS FOR ALL SEASONS"""

        seasons = []
        year = 1997

        while year <= 2016:
            seasons.append(self.url + str(year))
            year += 1

        final_stats = []
        for s in seasons:
            final_stats.append(self.season_stats(s))

        return final_stats


    def write_to_csv(self):

        """WRITE ALL STATS TO CSV"""

        lst = self.season_link()

        # WRITE TO CSV
        with open("Kobe_Bryant_stats.csv", "w", newline="", encoding="utf-8") as file:
            csv_writer = writer(file)

            # WRITE THE HEADERS FIRST
            csv_writer.writerow(["Date","Age","Game_result","Opponent","Points","Asists","Rebounds","Turnovers",
                                 "Steals","Blocks","Minutes_played","Fg_pct","Fg3_pct","Ft_pct","Season"])

            for row in lst:
                for match in row:
                    csv_writer.writerow(match)

        return "Csv file is ready"


print(Kobe().write_to_csv())





