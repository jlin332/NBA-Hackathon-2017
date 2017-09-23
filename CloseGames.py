from collections import defaultdict
from Queue import PriorityQueue
from operator import itemgetter
import csv

# for this file, we want to find games whose score difference between 2 teams are <-2 or >20
# return game id, players, period
def closeGames(filename):
    games = {'gameID': 'player'}
    # this dictionary stores for last row
    lastRow = {"id": "lastRowDiff"}
    with open(filename, 'rU') as f:
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
            lastRow[game_id] = int(homePts) - int(visitorPts)
            if (int(homePts) - int(visitorPts)
                    == 10 or int(homePts) - int(visitorPts) == -10) and int(period) == 4 and lastRow[game_id] <= 2:
                if not game_id in games.keys():
                    games[game_id] = [player1, player2, player3,
                                    player4, player5, player6, player7, player8, player9, player10]
            return games

def countFactors(gameDic, filename):
    with open(filename, 'rU') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        countDic = {'gameID':'list: contains 4 counts'}
        jumpShot2_count = 0
        jumpShot3_count = 0
        timeOut_count = 0
        driving_count = 0

        for row in reader:
            if row[0] not in countDic.keys():
                jumpShot3_count = 0
                jumpShot2_count = 0
                timeOut_count = 0
                driving_count = 0
            if row[0] in gameDic.keys() and int(row[11])== 4:
                if (row[29] == 'Jump Shot: Made'):
                    if row[25] == 2:
                        jumpShot2_count += 1
                    else:
                        jumpShot3_count += 1
                if 'Timeout' in row[29]:
                    timeOut_count += 1
                if row[29] == 'Driving Layup: Made':
                    driving_count += 1
                countDic[row[0]] = (jumpShot2_count, jumpShot3_count, timeOut_count, driving_count)
    return countDic

if __name__ == '__main__':
    closeGames('Play_by_Play_New.csv')
    # print games.__len__()




