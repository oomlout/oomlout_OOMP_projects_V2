
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9966"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9966"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB miniB Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB_miniB_Breakout')
    newPart['gitName'].append('USB_miniB_Breakout')
    newPart['eagleBoard'].append('/Hardware/SparkFun_miniUSB_Breakout_v13.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_miniUSB_Breakout_v13.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

