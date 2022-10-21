
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12650"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12650"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('AD8232 Heart Rate Monitor')
    newPart['gitRepo'].append('https://github.com/sparkfun/AD8232_Heart_Rate_Monitor')
    newPart['gitName'].append('AD8232_Heart_Rate_Monitor')
    newPart['eagleBoard'].append('/Hardware/AD8232_Heart_Rate_Monitor.brd')
    newPart['eagleSchem'].append('/Hardware/AD8232_Heart_Rate_Monitor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

