
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1400"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1400"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Push Button Power Switch PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Push-Button-Power-Switch-PCB')
    newPart['gitName'].append('Adafruit-Push-Button-Power-Switch-PCB')
    newPart['eagleBoard'].append('/Adafruit Power Switch.brd')
    newPart['eagleSchem'].append('/Adafruit Power Switch.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

