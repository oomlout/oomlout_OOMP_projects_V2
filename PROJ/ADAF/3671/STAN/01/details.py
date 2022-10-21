
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3671"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3671"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit CSI or DSI Cable Extender Thingy for Raspberry Pi')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-CSI-or-DSI-Cable-Extender-Thingy-for-Raspberry-Pi')
    newPart['gitName'].append('Adafruit-CSI-or-DSI-Cable-Extender-Thingy-for-Raspberry-Pi')
    newPart['eagleBoard'].append('/DSI CSI Extender.brd')
    newPart['eagleSchem'].append('/DSI CSI Extender.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

