
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11561"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11561"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RaspiRobot')
    newPart['gitRepo'].append('https://github.com/sparkfun/RaspiRobot')
    newPart['gitName'].append('RaspiRobot')
    newPart['eagleBoard'].append('/hardware/RaspiRobot_Board.brd')
    newPart['eagleSchem'].append('/hardware/RaspiRobot_Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

