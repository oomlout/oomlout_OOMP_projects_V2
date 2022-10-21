
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4300"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4300"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Hallowing M4 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Hallowing-M4-PCB')
    newPart['gitName'].append('Adafruit-Hallowing-M4-PCB')
    newPart['eagleBoard'].append('/Adafruit Hallowing M4.brd')
    newPart['eagleSchem'].append('/Adafruit Hallowing M4.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

