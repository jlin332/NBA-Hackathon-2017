import csv

# for this file, we want to find games whose score difference between 2 teams are <-2 or >20
# return game id, players, period

homeTeamID = 0
avgRateDic = {}

def closeGames(filename):
    games = {'gameID': 'player'}
    # this dictionary stores for last row
    lastRow = {"id": "lastRowDiff"}
    with open(filename, 'rU') as f:
        reader = csv.reader(f, delimiter=",")
        row1 = next(reader)
        gameIDRow = 0
        playClockTimeRow = 0
        homePTSRow = 0
        visitorPTSRow = 0
        descriptionRow = 0
        homeTeamRow = 0
        visitorTeamRow = 0
        periodRow = 0
        counter = 0
        for attr in row1:
            if (attr == 'Game_id'):
                gameIDRow = counter
            elif (attr == 'Play_Clock_Time'):
                playClockTimeRow = counter
            elif (attr == 'Home_PTS'):
                homePTSRow = counter
            elif (attr == 'Visitor_PTS'):
                visitorPTSRow = counter
            elif (attr == 'Description'):
                descriptionRow = counter
            elif (attr == 'Home_Team_id'):
                homeTeamRow = counter
            elif (attr == 'Visitor_Team_id'):
                visitorTeamRow = counter
            elif(attr == 'Period'):
                periodRow = counter
            counter += 1
        temp_game_id = 20700001
        initialHomeScore = 0
        initialVisitorScore = 0
        visitorPts = 0
        endScore = 0
        catchingUpTeam = 0
        endHomeScore = 0
        endVisitorScore = 0
        startTime = 0
        homeTeamID = 0
        for row in reader:
            period = row[periodRow]
            if (period == '4'):
                game_id = row[gameIDRow]
                home_team_id = row[homeTeamRow]
                homeTeamID = home_team_id
                visitor_team_id = row[visitorTeamRow]
                homePts = row[homePTSRow]
                visitorPts = row[visitorPTSRow]
                playClockTime = row[playClockTimeRow]
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
                if (int(homePts) - int(visitorPts) == 10 and lastRow[game_id] <= 2):  # when the start of a run happens
                    if not game_id in games.keys():
                        catchingUpTeam = home_team_id
                        startTime = playClockTime
                        initialHomeScore = homePts
                        games[game_id] = [player1, player2, player3,
                            player4, player5, player6, player7, player8, player9, player10]
                if ((int(homePts) - int(visitorPts) == -10) and lastRow[game_id] <= 2):  # when the start of a run happens
                    if not game_id in games.keys():
                        catchingUpTeam = visitor_team_id
                        startTime = playClockTime
                        initialVisitorScore = visitorPts
                        games[game_id] = [player1, player2, player3,
                            player4, player5, player6, player7, player8, player9, player10]
                if (temp_game_id != game_id and temp_game_id in games.keys()):
                    avgRate = calculateAvgRate(catchingUpTeam, startTime, initialHomeScore, initialVisitorScore, endHomeScore, endVisitorScore)
                    avgRateDic[temp_game_id] = avgRate
                    startTime = 0
                    initialHomeScore = 0
                    initialVisitorScore = 0
                    endHomeScore = 0
                    endVisitorScore = 0
                temp_game_id = game_id
                endHomeScore = homePts
                endVisitorScore = visitorPts
        return games


def calculateAvgRate(catchingUpTeam, startTime, initialHomeScore, initialVisitorScore, endHomeScore, endVisitorScore):
    if (catchingUpTeam == homeTeamID):
        endScore = endHomeScore
        initialScore = initialHomeScore
    else:
        initialScore = initialVisitorScore
        endScore = endVisitorScore
    totalPoints = int(endScore) - int(initialScore)
    totalTimePlayed = float(startTime)
    if (totalTimePlayed == 0):
        print float(startTime)
        return 0
    else:
        rate = totalPoints/totalTimePlayed
    return rate

def countFactors(gameDic, filename):
    with open(filename, 'rU') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        jumpShot2_count = 0
        jumpShot3_count = 0
        timeOut_count = 0
        driving_count = 0

        for row in reader:
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
    return (jumpShot2_count, jumpShot3_count, timeOut_count, driving_count)

if __name__ == '__main__':
    games = closeGames('Play_by_Play_New.csv')
    print avgRateDic
    print len(avgRateDic)
    print len(games)
