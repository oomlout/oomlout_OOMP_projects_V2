
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15164"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15164"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic OpenLog')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_OpenLog')
    newPart['gitName'].append('Qwiic_OpenLog')
    newPart['eagleBoard'].append('/Hardware/Qwiic-OpenLog.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic-OpenLog.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

