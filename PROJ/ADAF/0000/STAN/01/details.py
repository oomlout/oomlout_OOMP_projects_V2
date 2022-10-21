
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0000"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0000"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Data Logger shield')
    newPart['gitRepo'].append('https://github.com/adafruit/Data-Logger-shield')
    newPart['gitName'].append('Data-Logger-shield')
    newPart['eagleBoard'].append('/Adafruit Datalogger Shield.brd')
    newPart['eagleSchem'].append('/Adafruit Datalogger Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

