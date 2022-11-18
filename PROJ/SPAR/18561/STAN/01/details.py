
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18561"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18561"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Blower Fan')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Blower_Fan')
    newPart['gitName'].append('Qwiic_Blower_Fan')
    newPart['eagleBoard'].append('/Hardware/qwiic_blower.brd')
    newPart['eagleSchem'].append('/Hardware/qwiic_blower.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

