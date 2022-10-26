
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9822"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9822"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB RS 485 Converter')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB_RS-485_Converter')
    newPart['gitName'].append('USB_RS-485_Converter')
    newPart['eagleBoard'].append('/Hardware/SparkFun_USB_RS485_Converter.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_USB_RS485_Converter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

