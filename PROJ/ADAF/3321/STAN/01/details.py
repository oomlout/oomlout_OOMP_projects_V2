
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3321"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3321"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Mini TFT with Joystick Featherwing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Mini-TFT-with-Joystick-Featherwing-PCB')
    newPart['gitName'].append('Adafruit-Mini-TFT-with-Joystick-Featherwing-PCB')
    newPart['eagleBoard'].append('/Adafruit Mini TFT Wing.brd')
    newPart['eagleSchem'].append('/Adafruit Mini TFT Wing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

