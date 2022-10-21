
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17375"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17375"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic PIR')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_PIR')
    newPart['gitName'].append('Qwiic_PIR')
    newPart['eagleBoard'].append('/Hardware/Qwiic_PIR.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_PIR.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

