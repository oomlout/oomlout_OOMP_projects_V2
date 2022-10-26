
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3886"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3886"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MPU6050 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MPU6050-PCB')
    newPart['gitName'].append('Adafruit-MPU6050-PCB')
    newPart['eagleBoard'].append('/Adafruit MPU6050.brd')
    newPart['eagleSchem'].append('/Adafruit MPU6050.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

