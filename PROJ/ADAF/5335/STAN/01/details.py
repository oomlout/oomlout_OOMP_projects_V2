
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5335"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5335"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit CP2102N Friend PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-CP2102N-Friend-PCB')
    newPart['gitName'].append('Adafruit-CP2102N-Friend-PCB')
    newPart['eagleBoard'].append('/Adafruit CP2102N Friend.brd')
    newPart['eagleSchem'].append('/Adafruit CP2102N Friend.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

