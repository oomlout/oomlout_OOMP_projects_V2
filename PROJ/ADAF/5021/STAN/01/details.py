
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5021"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5021"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Slider Trinkey PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Slider-Trinkey-PCB')
    newPart['gitName'].append('Adafruit-Slider-Trinkey-PCB')
    newPart['eagleBoard'].append('/Adafruit Slider Trinkey.brd')
    newPart['eagleSchem'].append('/Adafruit Slider Trinkey.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

