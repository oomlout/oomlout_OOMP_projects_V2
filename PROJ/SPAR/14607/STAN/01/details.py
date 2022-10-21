
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14607"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14607"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic GRIDEye')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_GRIDEye')
    newPart['gitName'].append('Qwiic_GRIDEye')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Grideye.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Grideye.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

