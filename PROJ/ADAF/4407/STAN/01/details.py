
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4407"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4407"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MLX90640 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MLX90640-PCB')
    newPart['gitName'].append('Adafruit-MLX90640-PCB')
    newPart['eagleBoard'].append('/Adafruit MLX90640 IR Thermal Camera.brd')
    newPart['eagleSchem'].append('/Adafruit MLX90640 IR Thermal Camera.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

