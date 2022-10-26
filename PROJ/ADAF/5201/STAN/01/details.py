
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5201"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5201"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit IS31FL3741 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-IS31FL3741-PCB')
    newPart['gitName'].append('Adafruit-IS31FL3741-PCB')
    newPart['eagleBoard'].append('/Adafruit IS31FL3741 Matrix.brd')
    newPart['eagleSchem'].append('/Adafruit IS31FL3741 Matrix.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

