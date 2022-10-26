
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0395"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0395"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TXB0108 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TXB0108-PCB')
    newPart['gitName'].append('Adafruit-TXB0108-PCB')
    newPart['eagleBoard'].append('/Adafruit TXB0108.brd')
    newPart['eagleSchem'].append('/Adafruit TXB0108.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

