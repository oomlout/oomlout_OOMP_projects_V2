
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14785"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14785"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Pro RF')
    newPart['gitRepo'].append('https://github.com/sparkfun/Pro_RF')
    newPart['gitName'].append('Pro_RF')
    newPart['eagleBoard'].append('/Hardware/Pro_RF.brd')
    newPart['eagleSchem'].append('/Hardware/Pro_RF.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

