
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13777"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13777"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Battery Babysitter')
    newPart['gitRepo'].append('https://github.com/sparkfun/Battery_Babysitter')
    newPart['gitName'].append('Battery_Babysitter')
    newPart['eagleBoard'].append('/Hardware/sparkfun-battery-babysitter.brd')
    newPart['eagleSchem'].append('/Hardware/sparkfun-battery-babysitter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

