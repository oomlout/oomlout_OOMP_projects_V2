
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0757"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0757"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('4 Channel Level Shifter PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/4-Channel-Level-Shifter-PCB')
    newPart['gitName'].append('4-Channel-Level-Shifter-PCB')
    newPart['eagleBoard'].append('/Adafruit FET 4-Channel Shifter.brd')
    newPart['eagleSchem'].append('/Adafruit FET 4-Channel Shifter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

