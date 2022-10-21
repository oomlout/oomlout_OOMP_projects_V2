
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1981"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1981"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Flora Si1145 Light Sensor PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Flora-Si1145-Light-Sensor-PCB')
    newPart['gitName'].append('Adafruit-Flora-Si1145-Light-Sensor-PCB')
    newPart['eagleBoard'].append('/Adafruit Flora Si1145.brd')
    newPart['eagleSchem'].append('/Adafruit Flora Si1145.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

