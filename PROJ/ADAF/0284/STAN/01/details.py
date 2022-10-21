
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0284"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0284"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit FTDI Friend PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_FTDI-Friend-PCB')
    newPart['gitName'].append('Adafruit_FTDI-Friend-PCB')
    newPart['eagleBoard'].append('/ftdifriend.brd')
    newPart['eagleSchem'].append('/ftdifriend.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

