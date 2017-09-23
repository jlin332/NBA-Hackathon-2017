import csv
from CloseGames import closeGames

maxRate = 0
homeMaxRate = 0
homePlayClockTime = 0
visitorMaxRate = 0
visitorPlayClockTime = 0

rateDic = {}  # store gameID as key and dictionary { attribute , value of attribute}

dicList = []
specificationDic = {
    'Max_Rate': 0,
    'Play_Clock_Time': 0,
    'Highest_Rate_Home': 0,
    'Highest_Rate_Visitor': 0,
}

filteredDic = {}

def findGamewithRateFile(filename):
    with open(filename, 'rU') as f:
        reader = csv.reader(f, delimiter=",")
        row1 = next(reader)
        gameIDRow = 0
        playClockTimeRow = 0
        homePTSRow = 0
        visitorPTSRow = 0
        descriptionRow = 0
        shotValueRow = 0
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
            elif (attr == 'Shot_Value'):
                shotValueRow = counter
            elif(attr == 'Period'):
                periodRow = counter
            counter += 1
        temp_game_id = 20700001
        homeMaxRate = 0
        visitorMaxRate = 0
        homePlayClockTime = 0
        visitorPlayClockTime = 0
        initialHomeScore = 0
        initialVisitorScore = 0
        for row in reader:
            period = row[periodRow]
            if (period == '4'):
                game_id = row[gameIDRow]
                playClockTime = row[playClockTimeRow]
                homePTS = row[homePTSRow]
                visitorPTS = row[visitorPTSRow]
                description = row[descriptionRow]
                shotValue = row[shotValueRow]
                if (initialHomeScore == 0):
                    initialHomeScore = homePTS
                if (initialVisitorScore == 0):
                    initialVisitorScore = visitorPTS
                currentHomeRate = calculateRate(homePTS, initialHomeScore, playClockTime)
                currentVistorRate = calculateRate(visitorPTS, initialVisitorScore, playClockTime)
                if (currentHomeRate > homeMaxRate):
                    homeMaxRate = currentHomeRate
                    homePlayClockTime = playClockTime
                if (currentVistorRate > visitorMaxRate):
                    visitorMaxRate = currentHomeRate
                    visitorPlayClockTime = playClockTime
                if (temp_game_id != game_id):
                    rateDic[temp_game_id] = determineMax(homeMaxRate, homePlayClockTime, visitorMaxRate, visitorPlayClockTime)
                    homeMaxRate = 0
                    homePlayClockTime = 0
                    visitorMaxRate = 0
                    visitorPlayClockTime = 0
                    maxRate = 0
                    initialHomeScore = 0
                    initialVisitorScore = 0
                temp_game_id = game_id


def calculateRate(score, initialScore, playClockTime):
    timeElapsed = 720 - int(float(playClockTime))
    if (timeElapsed == 0):
        return 0
    else:
        score = float(score)
        initialScore = float(initialScore)
        rate = (score - initialScore)/timeElapsed
    return rate


def determineMax(homeMaxRate, homePlayClockTime, visitorMaxRate, visitorPlayClockTime):
    specDic = dict()
    if (homeMaxRate > visitorMaxRate):
        specDic['PlayClockTime'] = homePlayClockTime
        maxRate = homeMaxRate
        specDic['Max_Rate'] = maxRate
        specDic['Highest_Rate_Home'] = homeMaxRate
        specDic['Highest_Rate_Visitor'] = visitorMaxRate
    else:
        specDic['PlayClockTime'] = visitorPlayClockTime
        maxRate = visitorMaxRate
        specDic['Max_Rate'] = maxRate
        specDic['Highest_Rate_Home'] = homeMaxRate
        specDic['Highest_Rate_Visitor'] = visitorMaxRate
    return specDic

def filterCloseGames(closeGames, rateGames):
    for key in closeGames.keys():
        if key in rateGames.keys():
            spec = rateGames.get(key)
            filteredDic[key] = spec


findGamewithRateFile('Play_By_Play_New.csv')
games = closeGames('Play_By_Play_New.csv')
filterCloseGames(games, rateDic)
print len(filteredDic)
