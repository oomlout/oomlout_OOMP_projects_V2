
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14459"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14459"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Hat for Raspberry Pi')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Hat_for_Raspberry_Pi')
    newPart['gitName'].append('Qwiic_Hat_for_Raspberry_Pi')
    newPart['eagleBoard'].append('/Hardware/Qwiic Shield for RaspberryPi.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Shield for RaspberryPi.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

