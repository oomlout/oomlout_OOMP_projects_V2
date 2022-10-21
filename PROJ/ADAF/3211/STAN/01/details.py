
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3211"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3211"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit RGB Matrix Bonnet PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-RGB-Matrix-Bonnet-PCB')
    newPart['gitName'].append('Adafruit-RGB-Matrix-Bonnet-PCB')
    newPart['eagleBoard'].append('/Adafruit RGB Matrix Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit RGB Matrix Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

