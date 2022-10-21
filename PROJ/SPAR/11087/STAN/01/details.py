
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11087"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11087"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Uh Oh Battery Indicator')
    newPart['gitRepo'].append('https://github.com/sparkfun/Uh-Oh_Battery_Indicator')
    newPart['gitName'].append('Uh-Oh_Battery_Indicator')
    newPart['eagleBoard'].append('/hardware/Uh-Oh Battery Indicator.brd')
    newPart['eagleSchem'].append('/hardware/Uh-Oh Battery Indicator.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

