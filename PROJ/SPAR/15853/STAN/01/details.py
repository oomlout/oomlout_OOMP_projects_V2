
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15853"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15853"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic FM Transceiver Si4721')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_FM_Transceiver_Si4721')
    newPart['gitName'].append('Qwiic_FM_Transceiver_Si4721')
    newPart['eagleBoard'].append('/Hardware/Qwiic_FM_Transceiver_Si4721.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_FM_Transceiver_Si4721.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

