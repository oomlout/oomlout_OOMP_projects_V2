
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11512"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11512"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SN74HC165 Shift In Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/SN74HC165-Shift-In-Breakout')
    newPart['gitName'].append('SN74HC165-Shift-In-Breakout')
    newPart['eagleBoard'].append('/hardware/SN74HC165 Shift-In Breakout-v12.brd')
    newPart['eagleSchem'].append('/hardware/SN74HC165 Shift-In Breakout-v12.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

