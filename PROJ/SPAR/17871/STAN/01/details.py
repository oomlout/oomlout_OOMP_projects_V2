
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17871"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17871"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic KX13X')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_KX13X')
    newPart['gitName'].append('Qwiic_KX13X')
    newPart['eagleBoard'].append('/Hardware/Qwiic_KX13X.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_KX13X.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

