
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13687"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13687"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MyoWare Cable Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/MyoWare_Cable_Shield')
    newPart['gitName'].append('MyoWare_Cable_Shield')
    newPart['eagleBoard'].append('/Hardware/MyoWare_Cable_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/MyoWare_Cable_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

