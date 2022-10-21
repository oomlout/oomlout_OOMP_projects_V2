
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14779"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14779"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LumiDrive')
    newPart['gitRepo'].append('https://github.com/sparkfun/LumiDrive')
    newPart['gitName'].append('LumiDrive')
    newPart['eagleBoard'].append('/HARDWARE/LumiDrive.brd')
    newPart['eagleSchem'].append('/HARDWARE/LumiDrive.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

