
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11890"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11890"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MiniMoto')
    newPart['gitRepo'].append('https://github.com/sparkfun/MiniMoto')
    newPart['gitName'].append('MiniMoto')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MiniMoto.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MiniMoto.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

