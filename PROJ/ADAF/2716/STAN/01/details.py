
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2716"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2716"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit SPW2430 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-SPW2430-PCB')
    newPart['gitName'].append('Adafruit-SPW2430-PCB')
    newPart['eagleBoard'].append('/SPW2430-Silicon-Mic_Rev-B.brd')
    newPart['eagleSchem'].append('/SPW2430-Silicon-Mic_Rev-B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

