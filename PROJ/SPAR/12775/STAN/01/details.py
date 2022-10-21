
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12775"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12775"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RFM69HCW Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/RFM69HCW_Breakout')
    newPart['gitName'].append('RFM69HCW_Breakout')
    newPart['eagleBoard'].append('/hardware/RFM69HCW_BOB.brd')
    newPart['eagleSchem'].append('/hardware/RFM69HCW_BOB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

