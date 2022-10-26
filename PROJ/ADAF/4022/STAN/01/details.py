
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4022"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4022"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MLX90393 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MLX90393-PCB')
    newPart['gitName'].append('Adafruit-MLX90393-PCB')
    newPart['eagleBoard'].append('/Adafruit MLX90393 QT.brd')
    newPart['eagleSchem'].append('/Adafruit MLX90393 QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

