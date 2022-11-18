
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14733"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14733"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic RGB BH1749')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_RGB_BH1749')
    newPart['gitName'].append('Qwiic_RGB_BH1749')
    newPart['eagleBoard'].append('/Hardware/Qwiic RGB Sensor - BH1749.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic RGB Sensor - BH1749.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

