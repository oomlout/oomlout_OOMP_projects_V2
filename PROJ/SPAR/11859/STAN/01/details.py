
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11859"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11859"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('TMP006 Temp Sensor Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/TMP006-Temp_Sensor_Breakout')
    newPart['gitName'].append('TMP006-Temp_Sensor_Breakout')
    newPart['eagleBoard'].append('/hardware/TMP006 Breakout.brd')
    newPart['eagleSchem'].append('/hardware/TMP006 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

