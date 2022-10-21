
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2340"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2340"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Capacitive Touch HAT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Capacitive-Touch-HAT-PCB')
    newPart['gitName'].append('Adafruit-Capacitive-Touch-HAT-PCB')
    newPart['eagleBoard'].append('/Adafruit Capacitive Touch HAT.brd')
    newPart['eagleSchem'].append('/Adafruit Capacitive Touch HAT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

