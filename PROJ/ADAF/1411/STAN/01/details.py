
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1411"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1411"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 16 channel PWM Servo Shield')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-16-channel-PWM-Servo-Shield')
    newPart['gitName'].append('Adafruit-16-channel-PWM-Servo-Shield')
    newPart['eagleBoard'].append('/Adafruit PWM Servo Shield.brd')
    newPart['eagleSchem'].append('/Adafruit PWM Servo Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

