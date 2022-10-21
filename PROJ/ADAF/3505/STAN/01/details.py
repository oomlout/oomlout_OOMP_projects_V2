
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3505"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3505"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Metro M0 Express PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Metro-M0-Express-PCB')
    newPart['gitName'].append('Adafruit-Metro-M0-Express-PCB')
    newPart['eagleBoard'].append('/Adafruit Metro M0 Express.brd')
    newPart['eagleSchem'].append('/Adafruit Metro M0 Express.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

