
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10255"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10255"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LiPower Boost Converter')
    newPart['gitRepo'].append('https://github.com/sparkfun/LiPower_Boost_Converter')
    newPart['gitName'].append('LiPower_Boost_Converter')
    newPart['eagleBoard'].append('/HARDWARE/Li_Power_Boost_Converter.brd')
    newPart['eagleSchem'].append('/HARDWARE/Li_Power_Boost_Converter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

