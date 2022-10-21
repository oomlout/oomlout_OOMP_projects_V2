
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2899"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2899"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit VEML6070 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-VEML6070-PCB')
    newPart['gitName'].append('Adafruit-VEML6070-PCB')
    newPart['eagleBoard'].append('/Adafruit VEML6070.brd')
    newPart['eagleSchem'].append('/Adafruit VEML6070.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

