
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3297"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3297"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DRV8833 Motor Driver Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DRV8833-Motor-Driver-Breakout-PCB')
    newPart['gitName'].append('Adafruit-DRV8833-Motor-Driver-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit DRV8833.brd')
    newPart['eagleSchem'].append('/Adafruit DRV8833.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

