
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2130"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2130"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PAM8302 Mono Amplifier PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PAM8302-Mono-Amplifier-PCB')
    newPart['gitName'].append('Adafruit-PAM8302-Mono-Amplifier-PCB')
    newPart['eagleBoard'].append('/Adafruit PAM8302.brd')
    newPart['eagleSchem'].append('/Adafruit PAM8302.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

