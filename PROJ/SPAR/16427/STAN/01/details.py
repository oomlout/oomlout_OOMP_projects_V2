
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16427"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16427"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Alphanumeric Display')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Alphanumeric_Display')
    newPart['gitName'].append('Qwiic_Alphanumeric_Display')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Alphanumeric_Display.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Alphanumeric_Display.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

