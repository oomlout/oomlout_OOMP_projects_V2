
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10050"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10050"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('WiFly GSX Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/WiFly_GSX_Breakout')
    newPart['gitName'].append('WiFly_GSX_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_WiFly_GSX_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_WiFly_GSX_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

