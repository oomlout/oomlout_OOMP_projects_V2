
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5626"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5626"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PCA9548 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PCA9548-PCB')
    newPart['gitName'].append('Adafruit-PCA9548-PCB')
    newPart['eagleBoard'].append('/PCA9548A QT Board.brd')
    newPart['eagleSchem'].append('/PCA9548A QT Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

