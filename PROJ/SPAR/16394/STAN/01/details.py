
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16394"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16394"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Iridium 9603N')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Iridium_9603N')
    newPart['gitName'].append('Qwiic_Iridium_9603N')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Iridium_9603N.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Iridium_9603N.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

