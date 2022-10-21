
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1716"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1716"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Qualia Driver PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Qualia-Driver-PCB')
    newPart['gitName'].append('Adafruit-Qualia-Driver-PCB')
    newPart['eagleBoard'].append('/Adafruit Qualia Driver.brd')
    newPart['eagleSchem'].append('/Adafruit Qualia Driver.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

