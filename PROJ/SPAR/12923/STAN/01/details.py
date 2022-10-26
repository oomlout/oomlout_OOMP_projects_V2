
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12923"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12923"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroView')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroView')
    newPart['gitName'].append('MicroView')
    newPart['eagleBoard'].append('/Hardware/MicroView/SparkFun_MicroView.brd')
    newPart['eagleSchem'].append('/Hardware/MicroView/SparkFun_MicroView.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

