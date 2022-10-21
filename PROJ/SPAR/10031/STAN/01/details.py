
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10031"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10031"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB microB Plug Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB_microB_Plug_Breakout')
    newPart['gitName'].append('USB_microB_Plug_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_USB_MicroB_Plug_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_USB_MicroB_Plug_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

