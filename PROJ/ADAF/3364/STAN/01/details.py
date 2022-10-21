
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3364"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3364"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit pIRKey PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-pIRKey-PCB')
    newPart['gitName'].append('Adafruit-pIRKey-PCB')
    newPart['eagleBoard'].append('/Adafruit pIRkeyboard.brd')
    newPart['eagleSchem'].append('/Adafruit pIRkeyboard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

