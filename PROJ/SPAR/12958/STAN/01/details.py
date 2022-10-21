
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12958"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12958"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Electric Imp imp002 Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Electric_Imp_imp002_Breakout')
    newPart['gitName'].append('Electric_Imp_imp002_Breakout')
    newPart['eagleBoard'].append('/Hardware/Electric_Imp_imp002_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/Electric_Imp_imp002_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

