
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15444"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15444"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedBoard Artemis')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedBoard_Artemis')
    newPart['gitName'].append('RedBoard_Artemis')
    newPart['eagleBoard'].append('/Hardware/RedBoard-Artemis.brd')
    newPart['eagleSchem'].append('/Hardware/RedBoard-Artemis.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

