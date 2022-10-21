
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4832"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4832"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit HTU31 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-HTU31-PCB')
    newPart['gitName'].append('Adafruit-HTU31-PCB')
    newPart['eagleBoard'].append('/Adafruit HTU31D.brd')
    newPart['eagleSchem'].append('/Adafruit HTU31D.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

