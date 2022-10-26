
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13714"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13714"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('FreeSoc2')
    newPart['gitRepo'].append('https://github.com/sparkfun/FreeSoc2')
    newPart['gitName'].append('FreeSoc2')
    newPart['eagleBoard'].append('/Hardware/SparkFun_FreeSoC2.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_FreeSoC2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

