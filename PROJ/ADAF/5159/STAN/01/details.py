
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5159"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5159"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TCA4307 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TCA4307-PCB')
    newPart['gitName'].append('Adafruit-TCA4307-PCB')
    newPart['eagleBoard'].append('/Adafruit TCA4307.brd')
    newPart['eagleSchem'].append('/Adafruit TCA4307.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

