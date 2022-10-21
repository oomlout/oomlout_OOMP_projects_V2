
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2268"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2268"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Particle Spark Neopixel Ring PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Particle-Spark-Neopixel-Ring-PCB')
    newPart['gitName'].append('Adafruit-Particle-Spark-Neopixel-Ring-PCB')
    newPart['eagleBoard'].append('/Adafruit_NeoParticle24.brd')
    newPart['eagleSchem'].append('/Adafruit_NeoParticle24.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

