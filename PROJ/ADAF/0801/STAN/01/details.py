
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0801"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0801"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Prototyping Pi Plate PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Prototyping-Pi-Plate-PCB')
    newPart['gitName'].append('Adafruit-Prototyping-Pi-Plate-PCB')
    newPart['eagleBoard'].append('/Adafruit proto pi plate.brd')
    newPart['eagleSchem'].append('/Adafruit proto pi plate.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

