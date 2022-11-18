
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14767"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14767"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Pressure LPS25HB')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Pressure-LPS25HB')
    newPart['gitName'].append('Qwiic_Pressure-LPS25HB')
    newPart['eagleBoard'].append('/Hardware/Qwiic Pressure Sensor - LPS25HB.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Pressure Sensor - LPS25HB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

