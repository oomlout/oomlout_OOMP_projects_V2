
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12886"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12886"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Electric Imp Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/Electric_Imp_Breakout')
    newPart['gitName'].append('Electric_Imp_Breakout')
    newPart['eagleBoard'].append('/hardware/electric-imp-breakout.brd')
    newPart['eagleSchem'].append('/hardware/electric-imp-breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

