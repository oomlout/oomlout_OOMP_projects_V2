
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2024"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2024"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MPR121 Capacitive Touch Shield PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MPR121-Capacitive-Touch-Shield-PCB')
    newPart['gitName'].append('Adafruit-MPR121-Capacitive-Touch-Shield-PCB')
    newPart['eagleBoard'].append('/Adafruit MPR121 Capacitive Touch Shield.brd')
    newPart['eagleSchem'].append('/Adafruit MPR121 Capacitive Touch Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

