
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0199"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0199"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB Serial GPIO Breakout CP2103')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB_Serial_GPIO_Breakout-CP2103')
    newPart['gitName'].append('USB_Serial_GPIO_Breakout-CP2103')
    newPart['eagleBoard'].append('/Hardware/SparkFun_CP2103_Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_CP2103_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

