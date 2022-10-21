
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1712"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1712"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TPA2016 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TPA2016-PCB')
    newPart['gitName'].append('Adafruit-TPA2016-PCB')
    newPart['eagleBoard'].append('/Adafruit TPA2016D2.brd')
    newPart['eagleSchem'].append('/Adafruit TPA2016D2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

