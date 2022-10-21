
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14891"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14891"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('gator starter')
    newPart['gitRepo'].append('https://github.com/sparkfun/gator_starter')
    newPart['gitName'].append('gator_starter')
    newPart['eagleBoard'].append('/Hardware/gatorBytes_Sensor_board.brd')
    newPart['eagleSchem'].append('/Hardware/gatorBytes_Sensor_board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

