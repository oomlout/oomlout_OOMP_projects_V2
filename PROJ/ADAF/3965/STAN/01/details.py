
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3965"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3965"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MPRLS Pressure Sensor Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MPRLS-Pressure-Sensor-Breakout-PCB')
    newPart['gitName'].append('Adafruit-MPRLS-Pressure-Sensor-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit MPR pressure sensor.brd')
    newPart['eagleSchem'].append('/Adafruit MPR pressure sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

