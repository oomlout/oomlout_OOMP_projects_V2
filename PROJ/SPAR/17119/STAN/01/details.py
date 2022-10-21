
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17119"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17119"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Shield for Teensy')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Shield_for_Teensy')
    newPart['gitName'].append('Qwiic_Shield_for_Teensy')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Shield_for_Teensy.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Shield_for_Teensy.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

