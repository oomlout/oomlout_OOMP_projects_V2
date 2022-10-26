
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14691"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14691"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Transparent OLED HUD')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Transparent_OLED_HUD')
    newPart['gitName'].append('Qwiic_Transparent_OLED_HUD')
    newPart['eagleBoard'].append('/Hardware/QwiicHUD.brd')
    newPart['eagleSchem'].append('/Hardware/QwiicHUD.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

