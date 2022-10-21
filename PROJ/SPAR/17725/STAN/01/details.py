
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17725"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17725"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Asset Tracker Update Tool')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Asset_Tracker_Update_Tool')
    newPart['gitName'].append('MicroMod_Asset_Tracker_Update_Tool')
    newPart['eagleBoard'].append('/Hardware/MicroMod_Asset_Tracker_Firmware_Update_Tool.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod_Asset_Tracker_Firmware_Update_Tool.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

