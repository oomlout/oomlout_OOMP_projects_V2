
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9168"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9168"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('On Screen Display Breakout MAX7456')
    newPart['gitRepo'].append('https://github.com/sparkfun/On_Screen_Display_Breakout-MAX7456')
    newPart['gitName'].append('On_Screen_Display_Breakout-MAX7456')
    newPart['eagleBoard'].append('/Hardware/SparkFun_On_Screen_Display-MAX7456.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_On_Screen_Display-MAX7456.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

