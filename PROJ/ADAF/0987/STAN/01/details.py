
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0987"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0987"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MAX98306 Class D Amp PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MAX98306-Class-D-Amp-PCB')
    newPart['gitName'].append('Adafruit-MAX98306-Class-D-Amp-PCB')
    newPart['eagleBoard'].append('/Adafruit MAX98306.brd')
    newPart['eagleSchem'].append('/Adafruit MAX98306.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

