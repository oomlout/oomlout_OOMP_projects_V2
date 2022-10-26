
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1362"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1362"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Standalone Capacitive Sensor PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Standalone-Capacitive-Sensor-PCB')
    newPart['gitName'].append('Adafruit-Standalone-Capacitive-Sensor-PCB')
    newPart['eagleBoard'].append('/Adafruit AT42QT1010 Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit AT42QT1010 Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

