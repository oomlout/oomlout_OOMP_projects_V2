
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1393"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1393"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Sharp Memory Display PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Sharp-Memory-Display-PCBs')
    newPart['gitName'].append('Adafruit-Sharp-Memory-Display-PCBs')
    newPart['eagleBoard'].append('/Adafruit 2.7in Sharp Memory Display.brd')
    newPart['eagleSchem'].append('/Adafruit 2.7in Sharp Memory Display.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

