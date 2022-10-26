
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3463"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3463"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit FXOS8700 FXAS21002 9 DoF Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-FXOS8700-FXAS21002-9-DoF-Breakout-PCB')
    newPart['gitName'].append('Adafruit-FXOS8700-FXAS21002-9-DoF-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit FXOS8700 FXAS21002 9 DoF Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit FXOS8700 FXAS21002 9 DoF Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

