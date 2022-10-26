
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14997"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14997"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LTE Cat M1 Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/LTE_Cat_M1_Shield')
    newPart['gitName'].append('LTE_Cat_M1_Shield')
    newPart['eagleBoard'].append('/Hardware/lte_cat_m1_shield_sara-r4.brd')
    newPart['eagleSchem'].append('/Hardware/lte_cat_m1_shield_sara-r4.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

