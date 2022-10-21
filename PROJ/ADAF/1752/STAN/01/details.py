
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1752"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1752"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MAX9744 Amplifier PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MAX9744-Amplifier-PCB')
    newPart['gitName'].append('Adafruit-MAX9744-Amplifier-PCB')
    newPart['eagleBoard'].append('/Adafruit MAX9744.brd')
    newPart['eagleSchem'].append('/Adafruit MAX9744.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

