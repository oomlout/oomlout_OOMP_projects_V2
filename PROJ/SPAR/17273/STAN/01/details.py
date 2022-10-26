
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17273"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17273"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('QuickLogic Thing Plus')
    newPart['gitRepo'].append('https://github.com/sparkfun/QuickLogic_Thing_Plus')
    newPart['gitName'].append('QuickLogic_Thing_Plus')
    newPart['eagleBoard'].append('/Hardware/Board Files/QTPLUS_V2_1.brd')
    newPart['eagleSchem'].append('/Hardware/Board Files/QTPLUS_V2_1.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

