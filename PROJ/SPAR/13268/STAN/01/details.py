
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13268"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13268"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Snappable P Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/Snappable_P-Board')
    newPart['gitName'].append('Snappable_P-Board')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Snappable_P-Board.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Snappable_P-Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

