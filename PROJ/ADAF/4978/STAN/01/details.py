
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4978"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4978"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoKey Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoKey-Breakout-PCB')
    newPart['gitName'].append('Adafruit-NeoKey-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit NeoKey Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit NeoKey Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

