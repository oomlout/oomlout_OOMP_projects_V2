
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15353"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15353"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun TPL5110 Nano Power Timer')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_TPL5110_Nano_Power_Timer')
    newPart['gitName'].append('SparkFun_TPL5110_Nano_Power_Timer')
    newPart['eagleBoard'].append('/Hardware/SparkFun_TPL5110_Nano_Power_Switch.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_TPL5110_Nano_Power_Switch.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

