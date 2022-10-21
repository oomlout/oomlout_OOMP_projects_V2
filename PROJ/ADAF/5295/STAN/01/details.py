
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5295"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5295"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoSlider PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoSlider-PCB')
    newPart['gitName'].append('Adafruit-NeoSlider-PCB')
    newPart['eagleBoard'].append('/Adafruit NeoSlider.brd')
    newPart['eagleSchem'].append('/Adafruit NeoSlider.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

