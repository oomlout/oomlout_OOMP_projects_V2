
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8777"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8777"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Temperature Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Temperature_Sensor')
    newPart['gitName'].append('LilyPad_Temperature_Sensor')
    newPart['eagleBoard'].append('/Hardware/LilyPad_Temperature_Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_Temperature_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

