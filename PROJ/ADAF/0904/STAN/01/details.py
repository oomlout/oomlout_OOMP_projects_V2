
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0904"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0904"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit INA219 Current Sensor PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-INA219-Current-Sensor-PCB')
    newPart['gitName'].append('Adafruit-INA219-Current-Sensor-PCB')
    newPart['eagleBoard'].append('/Adafruit INA219 STEMMA QT.brd')
    newPart['eagleSchem'].append('/Adafruit INA219 STEMMA QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

