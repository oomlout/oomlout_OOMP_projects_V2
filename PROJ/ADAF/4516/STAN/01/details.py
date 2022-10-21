
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4516"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4516"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Feather nRF52840 Sense PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Feather-nRF52840-Sense-PCB')
    newPart['gitName'].append('Adafruit-Feather-nRF52840-Sense-PCB')
    newPart['eagleBoard'].append('/Adafruit Feather nRF52840 Sense.brd')
    newPart['eagleSchem'].append('/Adafruit Feather nRF52840 Sense.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

