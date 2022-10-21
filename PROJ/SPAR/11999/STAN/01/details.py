
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11999"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11999"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RedBot Whisker Bumper')
    newPart['gitRepo'].append('https://github.com/sparkfun/RedBot_Whisker_Bumper')
    newPart['gitName'].append('RedBot_Whisker_Bumper')
    newPart['eagleBoard'].append('/Hardware/RedBot Whisker Bumper.brd')
    newPart['eagleSchem'].append('/Hardware/RedBot Whisker Bumper.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

