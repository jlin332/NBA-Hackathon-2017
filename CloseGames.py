from collections import defaultdict
from Queue import PriorityQueue
from operator import itemgetter
import csv

# for this file, we want to find games whose score difference between 2 teams are <-2 or >20
# return game id, players, period


if __name__ == '__main__':
    games = {'gameID': 'periodNplayer'}
    print "kim and xingxing best friends"

    with open('Play_by_Play_New.csv', 'rU') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for row in reader:
            game_id = row[0]
            period = row[11]
            homePts = row[19]
            visitorPts = row[20]
            player1 = row[30]
            player2 = row[31]
            player3 = row[32]
            player4 = row[33]
            player5 = row[34]
            player6 = row[35]
            player7 = row[36]
            player8 = row[37]
            player9 = row[38]
            player10 = row[39]
            if (int(homePts) - int(visitorPts)) >= 20 or int(homePts) - int(visitorPts) <= -20:
                games[game_id] = [period, player1, player2, player3,
                                  player4, player5, player6, player7, player8, player9, player10]
    # print games.keys()
    print games.__len__()







