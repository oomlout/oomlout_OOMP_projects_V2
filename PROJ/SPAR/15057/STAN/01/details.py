
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15057"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15057"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic AS3935 Lightning Detector')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_AS3935_Lightning_Detector')
    newPart['gitName'].append('Qwiic_AS3935_Lightning_Detector')
    newPart['eagleBoard'].append('/Hardware/Qwiic_AS3935_Lightning_Detector.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_AS3935_Lightning_Detector.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

