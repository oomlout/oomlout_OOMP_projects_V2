
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2927"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2927"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit DC Stepper Motor FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-DC-Stepper-Motor-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-DC-Stepper-Motor-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit DC+Stepper Wing.brd')
    newPart['eagleSchem'].append('/Adafruit DC+Stepper Wing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

