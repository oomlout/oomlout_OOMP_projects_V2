
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12700"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12700"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB Type A Female Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB_Type_A_Female_Breakout')
    newPart['gitName'].append('USB_Type_A_Female_Breakout')
    newPart['eagleBoard'].append('/Hardware/USB_Type_A_Female_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/USB_Type_A_Female_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

