
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0815"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0815"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 16 Channel PWM Servo Driver PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-16-Channel-PWM-Servo-Driver-PCB')
    newPart['gitName'].append('Adafruit-16-Channel-PWM-Servo-Driver-PCB')
    newPart['eagleBoard'].append('/Adafruit PCA9685 rev C.brd')
    newPart['eagleSchem'].append('/Adafruit PCA9685 rev C.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

