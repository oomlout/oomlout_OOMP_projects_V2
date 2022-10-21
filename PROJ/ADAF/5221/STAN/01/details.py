
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5221"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5221"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ANO Rotary Navigation Encoder Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ANO-Rotary-Navigation-Encoder-Breakout-PCB')
    newPart['gitName'].append('Adafruit-ANO-Rotary-Navigation-Encoder-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit ANO Rotary Encoder Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit ANO Rotary Encoder Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

