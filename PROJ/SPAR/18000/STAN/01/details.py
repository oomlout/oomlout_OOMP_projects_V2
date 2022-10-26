
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18000"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18000"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('QwiicBus MidPoint')
    newPart['gitRepo'].append('https://github.com/sparkfun/QwiicBus_MidPoint')
    newPart['gitName'].append('QwiicBus_MidPoint')
    newPart['eagleBoard'].append('/Hardware/SparkFun_QwiicBus-Midpoint.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_QwiicBus-Midpoint.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

