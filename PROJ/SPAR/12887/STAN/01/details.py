
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12887"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12887"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Electric Imp Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Electric_Imp_Shield')
    newPart['gitName'].append('Electric_Imp_Shield')
    newPart['eagleBoard'].append('/Hardware/electric-imp-shield.brd')
    newPart['eagleSchem'].append('/Hardware/electric-imp-shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

