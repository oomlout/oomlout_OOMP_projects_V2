
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17272"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17272"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Asset Tracker')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Asset_Tracker')
    newPart['gitName'].append('MicroMod_Asset_Tracker')
    newPart['eagleBoard'].append('/Hardware/MicroMod_Asset_Tracker.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod_Asset_Tracker.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

