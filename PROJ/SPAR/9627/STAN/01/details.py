
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9627"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9627"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Mini FET Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Mini_FET_Shield')
    newPart['gitName'].append('Mini_FET_Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Mini_FET_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Mini_FET_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

