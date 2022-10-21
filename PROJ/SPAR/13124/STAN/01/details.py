
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13124"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13124"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Proto Pedal')
    newPart['gitRepo'].append('https://github.com/sparkfun/Proto_Pedal')
    newPart['gitName'].append('Proto_Pedal')
    newPart['eagleBoard'].append('/Hardware/Proto_Pedal.brd')
    newPart['eagleSchem'].append('/Hardware/Proto_Pedal.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

