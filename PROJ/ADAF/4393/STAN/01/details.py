
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4393"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4393"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Mini PiTFT 240x135 TFT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Mini-PiTFT-240x135-TFT-PCB')
    newPart['gitName'].append('Adafruit-Mini-PiTFT-240x135-TFT-PCB')
    newPart['eagleBoard'].append('/Adafruit Mini PiTFT - 135x240 Color TFT.brd')
    newPart['eagleSchem'].append('/Adafruit Mini PiTFT - 135x240 Color TFT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

