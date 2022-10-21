
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13628"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13628"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Photon OLED Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/Photon_OLED_Shield')
    newPart['gitName'].append('Photon_OLED_Shield')
    newPart['eagleBoard'].append('/Hardware/Photon_Micro_OLED_Shield.brd')
    newPart['eagleSchem'].append('/Hardware/Photon_Micro_OLED_Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

