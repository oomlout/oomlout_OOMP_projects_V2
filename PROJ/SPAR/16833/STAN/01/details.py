
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16833"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16833"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Quad Solid State Relay')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Quad_Solid_State_Relay')
    newPart['gitName'].append('Qwiic_Quad_Solid_State_Relay')
    newPart['eagleBoard'].append('/Hardware/Qwiic Solid State Relay.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Solid State Relay.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

