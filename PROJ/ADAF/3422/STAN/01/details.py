
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3422"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3422"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Arcade Bonnet PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Arcade-Bonnet-PCB')
    newPart['gitName'].append('Adafruit-Arcade-Bonnet-PCB')
    newPart['eagleBoard'].append('/Adafruit Arcade Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit Arcade Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

