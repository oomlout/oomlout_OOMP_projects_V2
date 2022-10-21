
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1755"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1755"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LED Sequin PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LED-Sequin-PCB')
    newPart['gitName'].append('Adafruit-LED-Sequin-PCB')
    newPart['eagleBoard'].append('/Adafruit LED Sequin.brd')
    newPart['eagleSchem'].append('/Adafruit LED Sequin.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

