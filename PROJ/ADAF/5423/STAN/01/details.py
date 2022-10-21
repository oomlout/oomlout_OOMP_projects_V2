
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5423"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5423"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TSC2007 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TSC2007-PCB')
    newPart['gitName'].append('Adafruit-TSC2007-PCB')
    newPart['eagleBoard'].append('/Adafruit TSC2007.brd')
    newPart['eagleSchem'].append('/Adafruit TSC2007.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

