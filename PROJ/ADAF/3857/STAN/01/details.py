
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3857"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3857"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Feather M4 Express PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Feather-M4-Express-PCB')
    newPart['gitName'].append('Adafruit-Feather-M4-Express-PCB')
    newPart['eagleBoard'].append('/Adafruit Feather M4 Express.brd')
    newPart['eagleSchem'].append('/Adafruit Feather M4 Express.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

