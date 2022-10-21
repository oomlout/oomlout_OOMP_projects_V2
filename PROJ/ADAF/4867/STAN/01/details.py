
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4867"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4867"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit SCD 30 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-SCD-30-PCB')
    newPart['gitName'].append('Adafruit-SCD-30-PCB')
    newPart['eagleBoard'].append('/Adafruit SCD30.brd')
    newPart['eagleSchem'].append('/Adafruit SCD30.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

