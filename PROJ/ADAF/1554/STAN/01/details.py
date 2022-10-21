
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1554"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1554"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PCB Ruler')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PCB-Ruler')
    newPart['gitName'].append('Adafruit-PCB-Ruler')
    newPart['eagleBoard'].append('/Adafruit PCB Reference Ruler.brd')
    newPart['eagleSchem'].append('/Adafruit PCB Reference Ruler.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

