
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3333"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3333"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Circuit Playground Express PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Circuit-Playground-Express-PCB')
    newPart['gitName'].append('Adafruit-Circuit-Playground-Express-PCB')
    newPart['eagleBoard'].append('/Adafruit Circuit Playground Express.brd')
    newPart['eagleSchem'].append('/Adafruit Circuit Playground Express.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

