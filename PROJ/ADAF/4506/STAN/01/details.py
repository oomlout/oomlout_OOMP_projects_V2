
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4506"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4506"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 1.3in Color TFT Bonnet PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-1.3in-Color-TFT-Bonnet-PCB')
    newPart['gitName'].append('Adafruit-1.3in-Color-TFT-Bonnet-PCB')
    newPart['eagleBoard'].append('/Adafruit 1.3in Color TFT Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit 1.3in Color TFT Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

