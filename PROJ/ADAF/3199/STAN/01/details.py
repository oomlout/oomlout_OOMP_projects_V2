
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3199"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3199"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MiCS 5524 Gas Sensor Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MiCS-5524-Gas-Sensor-Breakout-PCB')
    newPart['gitName'].append('Adafruit-MiCS-5524-Gas-Sensor-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit MICS-5524.brd')
    newPart['eagleSchem'].append('/Adafruit MICS-5524.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

