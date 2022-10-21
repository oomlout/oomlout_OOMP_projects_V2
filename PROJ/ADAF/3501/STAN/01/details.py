
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3501"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3501"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Gemma M0 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Gemma-M0-PCB')
    newPart['gitName'].append('Adafruit-Gemma-M0-PCB')
    newPart['eagleBoard'].append('/Adafruit Gemma M0.brd')
    newPart['eagleSchem'].append('/Adafruit Gemma M0.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

