
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14334"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14334"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Module for Tessel 2')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Module_for_Tessel_2')
    newPart['gitName'].append('Qwiic_Module_for_Tessel_2')
    newPart['eagleBoard'].append('/Hardware/Qwiic Module for Tessel 2.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Module for Tessel 2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

