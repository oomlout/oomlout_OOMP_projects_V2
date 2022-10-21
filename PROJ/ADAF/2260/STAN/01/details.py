
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2260"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2260"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 5 HDMI Backpack PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-5-HDMI-Backpack-PCB')
    newPart['gitName'].append('Adafruit-5-HDMI-Backpack-PCB')
    newPart['eagleBoard'].append('/Adafruit 5in HDMI Backpack.brd')
    newPart['eagleSchem'].append('/Adafruit 5in HDMI Backpack.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

