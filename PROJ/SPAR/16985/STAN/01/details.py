
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16985"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16985"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Input and Display Carrier')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Input_and_Display_Carrier')
    newPart['gitName'].append('MicroMod_Input_and_Display_Carrier')
    newPart['eagleBoard'].append('/Hardware/SparkFun_MicroMod_Input_and_Display_Carrier.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_MicroMod_Input_and_Display_Carrier.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

