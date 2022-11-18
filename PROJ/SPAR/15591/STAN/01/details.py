
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15591"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15591"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Switch')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Switch')
    newPart['gitName'].append('Qwiic_Switch')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Switch.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Switch.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

