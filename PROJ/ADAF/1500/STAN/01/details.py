
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1500"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1500"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Trinket PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Trinket-PCB')
    newPart['gitName'].append('Adafruit-Trinket-PCB')
    newPart['eagleBoard'].append('/Adafruit Trinket 3.3V.brd')
    newPart['eagleSchem'].append('/Adafruit Trinket 3.3V.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

