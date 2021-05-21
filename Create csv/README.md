# Folder overview

This folder contains:

1) A python file that scrapes stats from Basketball Reference (https://www.basketball-reference.com/players/b/bryanko01.html) 
and writes them to a csv file
4) The csv file that is created

## Collecting the data

At first, i generated the url for every season in his career. I noticed that there is a pattern between the urls of each season. 

The base url was https://www.basketball-reference.com/players/b/bryanko01/gamelog/ . To create the url for each season i combined the base url with each year from 1997-2016 (From his first to last season). Each url was stored in a list

![image](https://user-images.githubusercontent.com/72921465/119197278-27c1c780-ba90-11eb-9a26-17ae0a2af71a.png)

To collect Kobe Bryant's stats for all his 1072 games I used **Beautiful Soup**.

1) Located the stats table

![image](https://user-images.githubusercontent.com/72921465/119197748-ed0c5f00-ba90-11eb-8c41-d019d1a87fc3.png)

2) Found all rows

![image](https://user-images.githubusercontent.com/72921465/119197800-ff869880-ba90-11eb-8ec8-b9acf0c5977c.png)

3) For each row i collected the following stats: Matchdate, Age, Game result, Opponent team, Points, Asists, Rebounds, Steals, Blocks, Turnovers, Field goal percentage, 3-Point field goal percentage, Free throw percentage, Minutes played, Season

4) I repeated the same technique for all his 20 seasons and using **Csv Writer** i wrote all stats to a csv file which is the output of the python file
