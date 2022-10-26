
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1580"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1580"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit AR1100 Resistive Touch Controller PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-AR1100-Resistive-Touch-Controller-PCB')
    newPart['gitName'].append('Adafruit-AR1100-Resistive-Touch-Controller-PCB')
    newPart['eagleBoard'].append('/Adafruit AR1100.brd')
    newPart['eagleSchem'].append('/Adafruit AR1100.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

