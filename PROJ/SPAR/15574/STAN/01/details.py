
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15574"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15574"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Artemis Thing Plus')
    newPart['gitRepo'].append('https://github.com/sparkfun/Artemis_Thing_Plus')
    newPart['gitName'].append('Artemis_Thing_Plus')
    newPart['eagleBoard'].append('/Hardware/Artemis Thing Plus.brd')
    newPart['eagleSchem'].append('/Hardware/Artemis Thing Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

