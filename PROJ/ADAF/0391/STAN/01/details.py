
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0391"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0391"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit BMP085 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-BMP085-PCB')
    newPart['gitName'].append('Adafruit-BMP085-PCB')
    newPart['eagleBoard'].append('/Adafruit_BMP085.brd')
    newPart['eagleSchem'].append('/Adafruit_BMP085.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

