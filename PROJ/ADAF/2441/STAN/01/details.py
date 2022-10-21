
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2441"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2441"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PiTFT 3.5 Plus PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PiTFT-3.5-Plus-PCB')
    newPart['gitName'].append('Adafruit-PiTFT-3.5-Plus-PCB')
    newPart['eagleBoard'].append('/Adafruit PiTFT Plus 3.5in.brd')
    newPart['eagleSchem'].append('/Adafruit PiTFT Plus 3.5in.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

