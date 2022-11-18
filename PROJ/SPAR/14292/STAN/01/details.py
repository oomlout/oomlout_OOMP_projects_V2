
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14292"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14292"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Shield for RaspberryPi')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Shield_for_RaspberryPi')
    newPart['gitName'].append('Qwiic_Shield_for_RaspberryPi')
    newPart['eagleBoard'].append('/Hardware/Qwiic Shield for RaspberryPi.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Shield for RaspberryPi.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

