
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16566"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16566"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Quad Relay')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Quad_Relay')
    newPart['gitName'].append('Qwiic_Quad_Relay')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Quad_Relay.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Quad_Relay.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

