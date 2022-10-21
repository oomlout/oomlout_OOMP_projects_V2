
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11113"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11113"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Pro Mini Candy')
    newPart['gitRepo'].append('https://github.com/sparkfun/Pro_Mini_Candy')
    newPart['gitName'].append('Pro_Mini_Candy')
    newPart['eagleBoard'].append('/Hardware/Pro-Mini-Candy.brd')
    newPart['eagleSchem'].append('/Hardware/Pro-Mini-Candy.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

