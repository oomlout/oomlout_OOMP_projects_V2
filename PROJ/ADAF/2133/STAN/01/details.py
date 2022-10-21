
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2133"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2133"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Audio FX Sound Board PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Audio-FX-Sound-Board-PCBs')
    newPart['gitName'].append('Adafruit-Audio-FX-Sound-Board-PCBs')
    newPart['eagleBoard'].append('/Adafruit EZ-SFX Mini.brd')
    newPart['eagleSchem'].append('/Adafruit EZ-SFX Mini.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

