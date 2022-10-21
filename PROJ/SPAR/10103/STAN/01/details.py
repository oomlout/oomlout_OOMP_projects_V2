
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10103"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10103"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Serial Alphanumeric Display Driver')
    newPart['gitRepo'].append('https://github.com/sparkfun/Serial_Alphanumeric_Display_Driver')
    newPart['gitName'].append('Serial_Alphanumeric_Display_Driver')
    newPart['eagleBoard'].append('/hardware/AlphaNumeric-Display-Driver.brd')
    newPart['eagleSchem'].append('/hardware/AlphaNumeric-Display-Driver.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

