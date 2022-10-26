
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15442"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15442"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedBoard Artemis ATP')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedBoard_Artemis_ATP')
    newPart['gitName'].append('RedBoard_Artemis_ATP')
    newPart['eagleBoard'].append('/Hardware/RedBoard-Artemis-ATP.brd')
    newPart['eagleSchem'].append('/Hardware/RedBoard-Artemis-ATP.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

