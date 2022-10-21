
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9267"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9267"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Accelerometer ADXL335')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Accelerometer-ADXL335')
    newPart['gitName'].append('LilyPad_Accelerometer-ADXL335')
    newPart['eagleBoard'].append('/Hardware/LilyPad-Accelerometer-v20.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad-Accelerometer-v20.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

