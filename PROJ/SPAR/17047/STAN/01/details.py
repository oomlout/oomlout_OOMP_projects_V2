
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17047"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17047"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic GPIO')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_GPIO')
    newPart['gitName'].append('Qwiic_GPIO')
    newPart['eagleBoard'].append('/Hardware/Qwiic_GPIO.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_GPIO.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

