
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12705"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12705"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ML8511 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/ML8511_Breakout')
    newPart['gitName'].append('ML8511_Breakout')
    newPart['eagleBoard'].append('/hardware/ML8511_Breakout.brd')
    newPart['eagleSchem'].append('/hardware/ML8511_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

