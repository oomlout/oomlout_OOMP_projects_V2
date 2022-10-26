
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1164"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1164"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit INA169 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-INA169-Breakout-PCB')
    newPart['gitName'].append('Adafruit-INA169-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit INA169 CurPowerMonitor.brd')
    newPart['eagleSchem'].append('/Adafruit INA169 CurPowerMonitor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

