
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1778"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1778"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit AD8495 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-AD8495-Breakout-PCB')
    newPart['gitName'].append('Adafruit-AD8495-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit AD849x_Thermo.brd')
    newPart['eagleSchem'].append('/Adafruit AD849x_Thermo.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

