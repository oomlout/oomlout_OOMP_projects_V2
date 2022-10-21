
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0376"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0376"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 2.8 Inch TFT Shield PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_2.8_Inch_TFT_Shield_PCB')
    newPart['gitName'].append('Adafruit_2.8_Inch_TFT_Shield_PCB')
    newPart['eagleBoard'].append('/tfttouchshield.brd')
    newPart['eagleSchem'].append('/tfttouchshield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

