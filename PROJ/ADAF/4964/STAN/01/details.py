
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4964"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4964"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Rotary Trinkey PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Rotary-Trinkey-PCB')
    newPart['gitName'].append('Adafruit-Rotary-Trinkey-PCB')
    newPart['eagleBoard'].append('/Adafruit Rotary Trinkey.brd')
    newPart['eagleSchem'].append('/Adafruit Rotary Trinkey.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

