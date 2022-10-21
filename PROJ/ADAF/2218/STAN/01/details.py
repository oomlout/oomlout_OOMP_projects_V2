
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2218"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2218"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TFP401 HDMI To 40Pin TFT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TFP401-HDMI-To-40Pin-TFT-PCB')
    newPart['gitName'].append('Adafruit-TFP401-HDMI-To-40Pin-TFT-PCB')
    newPart['eagleBoard'].append('/Adafruit TFP401 to 40pin TFT.brd')
    newPart['eagleSchem'].append('/Adafruit TFP401 to 40pin TFT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

