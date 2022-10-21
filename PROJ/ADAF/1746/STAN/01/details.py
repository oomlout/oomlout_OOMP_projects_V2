
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1746"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1746"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit HMC5883 Mag Compass Sensor PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-HMC5883-Mag-Compass-Sensor-PCB')
    newPart['gitName'].append('Adafruit-HMC5883-Mag-Compass-Sensor-PCB')
    newPart['eagleBoard'].append('/Adafruit HMC5883L Compass.brd')
    newPart['eagleSchem'].append('/Adafruit HMC5883L Compass.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

