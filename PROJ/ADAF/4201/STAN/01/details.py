
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4201"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4201"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit AirLift Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-AirLift-Breakout-PCB')
    newPart['gitName'].append('Adafruit-AirLift-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit AirLift Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit AirLift Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

