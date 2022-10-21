
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12885"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12885"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SunnyBuddy')
    newPart['gitRepo'].append('https://github.com/sparkfun/SunnyBuddy')
    newPart['gitName'].append('SunnyBuddy')
    newPart['eagleBoard'].append('/Hardware/SunnyBuddy.brd')
    newPart['eagleSchem'].append('/Hardware/SunnyBuddy.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

