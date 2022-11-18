
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14607"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14607"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic GridEye')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_GridEye')
    newPart['gitName'].append('Qwiic_GridEye')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Grideye.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Grideye.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

