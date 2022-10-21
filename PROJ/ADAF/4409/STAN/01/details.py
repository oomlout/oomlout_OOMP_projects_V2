
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4409"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4409"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit STEMMA Non Latching Mini Relay PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-STEMMA-Non-Latching-Mini-Relay-PCB')
    newPart['gitName'].append('Adafruit-STEMMA-Non-Latching-Mini-Relay-PCB')
    newPart['eagleBoard'].append('/Adafruit Non-Latching Relay Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit Non-Latching Relay Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

