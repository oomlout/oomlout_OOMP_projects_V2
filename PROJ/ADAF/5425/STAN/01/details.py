
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5425"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5425"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit VL53L4CX PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-VL53L4CX-PCB')
    newPart['gitName'].append('Adafruit-VL53L4CX-PCB')
    newPart['eagleBoard'].append('/Adafruit VL53L4CX.brd')
    newPart['eagleSchem'].append('/Adafruit VL53L4CX.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

