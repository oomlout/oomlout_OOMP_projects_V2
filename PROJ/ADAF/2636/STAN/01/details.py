
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2636"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2636"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit FONA808 Shield PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-FONA808-Shield-PCB')
    newPart['gitName'].append('Adafruit-FONA808-Shield-PCB')
    newPart['eagleBoard'].append('/Adafruit SIM808 Shield.brd')
    newPart['eagleSchem'].append('/Adafruit SIM808 Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

