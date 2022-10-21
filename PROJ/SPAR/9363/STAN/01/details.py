
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9363"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9363"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ColorLCDShield')
    newPart['gitRepo'].append('https://github.com/sparkfun/ColorLCDShield')
    newPart['gitName'].append('ColorLCDShield')
    newPart['eagleBoard'].append('/hardware/Color-LCD-Shield.brd')
    newPart['eagleSchem'].append('/hardware/Color-LCD-Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

