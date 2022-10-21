
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2348"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2348"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DC Stepper Motor HAT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DC-Stepper-Motor-HAT-PCB')
    newPart['gitName'].append('Adafruit-DC-Stepper-Motor-HAT-PCB')
    newPart['eagleBoard'].append('/Adafruit Motor Bonnet Rev A.brd')
    newPart['eagleSchem'].append('/Adafruit Motor Bonnet Rev A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

