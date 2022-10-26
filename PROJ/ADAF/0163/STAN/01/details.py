
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0163"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0163"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Analog Accelerometers PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Analog-Accelerometers-PCBs')
    newPart['gitName'].append('Adafruit-Analog-Accelerometers-PCBs')
    newPart['eagleBoard'].append('/Adafruit ADXL326.brd')
    newPart['eagleSchem'].append('/Adafruit ADXL326.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

