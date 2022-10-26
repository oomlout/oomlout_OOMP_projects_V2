
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14965"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14965"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LuMini 3 Inch')
    newPart['gitRepo'].append('https://github.com/sparkfun/LuMini_3_Inch')
    newPart['gitName'].append('LuMini_3_Inch')
    newPart['eagleBoard'].append('/Hardware/LuMini_3Inch.brd')
    newPart['eagleSchem'].append('/Hardware/LuMini_3Inch.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

