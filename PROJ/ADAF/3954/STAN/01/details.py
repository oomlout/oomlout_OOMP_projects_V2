
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3954"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3954"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoTrellis 4x4 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoTrellis-4x4-PCB')
    newPart['gitName'].append('Adafruit-NeoTrellis-4x4-PCB')
    newPart['eagleBoard'].append('/Adafruit NeoTrellis 4x4.brd')
    newPart['eagleSchem'].append('/Adafruit NeoTrellis 4x4.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

