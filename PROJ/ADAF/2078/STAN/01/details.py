
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2078"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2078"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PowerBoost 500 Shield PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PowerBoost-500-Shield-PCB')
    newPart['gitName'].append('Adafruit-PowerBoost-500-Shield-PCB')
    newPart['eagleBoard'].append('/Adafruit PowerBoost Shield.brd')
    newPart['eagleSchem'].append('/Adafruit PowerBoost Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

