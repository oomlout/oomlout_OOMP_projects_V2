
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "20167"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR20167"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('u blox ZED F9P NEO D9S Combo Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/u-blox_ZED-F9P_NEO-D9S_Combo_Breakout')
    newPart['gitName'].append('u-blox_ZED-F9P_NEO-D9S_Combo_Breakout')
    newPart['eagleBoard'].append('/Hardware/ZED-F9P_NEO-D9S_Combo.brd')
    newPart['eagleSchem'].append('/Hardware/ZED-F9P_NEO-D9S_Combo.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

