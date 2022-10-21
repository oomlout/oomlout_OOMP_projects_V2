
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2745"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2745"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LM3671 Buck Converter PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LM3671-Buck-Converter-PCB')
    newPart['gitName'].append('Adafruit-LM3671-Buck-Converter-PCB')
    newPart['eagleBoard'].append('/Adafruit LM3671 Buck.brd')
    newPart['eagleSchem'].append('/Adafruit LM3671 Buck.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

