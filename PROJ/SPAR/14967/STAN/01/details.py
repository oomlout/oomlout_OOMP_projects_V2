
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14967"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14967"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LuMini 1 Inch')
    newPart['gitRepo'].append('https://github.com/sparkfun/LuMini_1_Inch')
    newPart['gitName'].append('LuMini_1_Inch')
    newPart['eagleBoard'].append('/Hardware/14075-LuMini_1Inch-panel.brd')
    newPart['eagleSchem'].append('/Hardware/14075-LuMini_1Inch-panel.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

