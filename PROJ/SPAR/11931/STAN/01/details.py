
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11931"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11931"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Digital Temperature Sensor Breakout   TMP102')
    newPart['gitRepo'].append('https://github.com/sparkfun/Digital_Temperature_Sensor_Breakout_-_TMP102')
    newPart['gitName'].append('Digital_Temperature_Sensor_Breakout_-_TMP102')
    newPart['eagleBoard'].append('/Hardware/Digital Temperature Sensor Breakout - TMP102.brd')
    newPart['eagleSchem'].append('/Hardware/Digital Temperature Sensor Breakout - TMP102.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

