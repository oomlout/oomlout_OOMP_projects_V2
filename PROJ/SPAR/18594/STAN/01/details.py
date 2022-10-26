
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18594"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18594"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod DA16200 Function')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_DA16200_Function')
    newPart['gitName'].append('MicroMod_DA16200_Function')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MicroMod_DA16200_Function.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MicroMod_DA16200_Function.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

