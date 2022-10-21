
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1325"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1325"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit FPC SMT Adapter PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-FPC-SMT-Adapter-PCBs')
    newPart['gitName'].append('Adafruit-FPC-SMT-Adapter-PCBs')
    newPart['eagleBoard'].append('/1.0mm + 0.5mm FPC stick.brd')
    newPart['eagleSchem'].append('/1.0mm + 0.5mm FPC stick.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

