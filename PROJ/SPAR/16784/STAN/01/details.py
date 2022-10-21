
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16784"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16784"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Mux TCA9548A')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Mux_TCA9548A')
    newPart['gitName'].append('Qwiic_Mux_TCA9548A')
    newPart['eagleBoard'].append('/Hardware/Qwiic Mux.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Mux.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

