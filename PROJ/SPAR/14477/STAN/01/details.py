
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14477"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14477"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Shield for Photon')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Shield_for_Photon')
    newPart['gitName'].append('Qwiic_Shield_for_Photon')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Shield_for_Photon.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Shield_for_Photon.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

