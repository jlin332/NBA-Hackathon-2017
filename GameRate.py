import csv


maxRate = 0
homeMaxRate = 0
homePlayClockTime = 0
visitorMaxRate = 0
visitorPlayClockTime = 0

rateDic = {} #store gameID as key and dictionary { attribute , value of attribute}
specificationDic = {
    'Play_Clock_Time': 0,
    'Highest_Rate_Home': 0,
    'Highest_Rate_Visitor': 0,
}
shotDic = {}  #store shot value and general description


def findGamewithRate(filename):
    with open(filename, 'rU') as f:
        reader = csv.reader(f, delimiter=",")
        row1 = next(reader)
        gameIDRow = 0
        playClockTimeRow = 0
        homePTSRow = 0
        visitorPTSRow = 0
        descriptionRow = 0
        shotValueRow = 0
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
            counter += 1
        for row in reader:
            game_id = row[gameIDRow]
            playClockTime = row[playClockTimeRow]
            homePTS = row[homePTSRow]
            visitorPTS = row[visitorPTSRow]
            description = row[descriptionRow]
            shotValue = row[shotValueRow]
            currentHomeRate = calculateRate(homePTS, playClockTime)
            currentVistorRate = calculateRate(visitorPTS, playClockTime)
            if (currentHomeRate > homeMaxRate):
                homeMaxRate = currentHomeRate
            if (currentVistorRate > visitorMaxRate):
                visitorMaxRate = currentHomeRate


def calculateRate(int score, int playClockTime):
    int timeElapsed = 720 - playClockTime
    float rate = score/playClockTime
    return rate


findGamewithRate('Play_By_Play_New.csv')
