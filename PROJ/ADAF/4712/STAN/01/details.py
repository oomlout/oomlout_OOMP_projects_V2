
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4712"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4712"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LC709203F PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LC709203F-PCB')
    newPart['gitName'].append('Adafruit-LC709203F-PCB')
    newPart['eagleBoard'].append('/Adafruit LC709203F LiPoly LiIon Fuel Gauge and Battery Monitor.brd')
    newPart['eagleSchem'].append('/Adafruit LC709203F LiPoly LiIon Fuel Gauge and Battery Monitor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

