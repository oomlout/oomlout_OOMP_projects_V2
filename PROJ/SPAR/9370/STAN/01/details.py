
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9370"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9370"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('DC DC Converter Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/DC-DC_Converter_Breakout')
    newPart['gitName'].append('DC-DC_Converter_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_DC-DC_Converter_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_DC-DC_Converter_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

