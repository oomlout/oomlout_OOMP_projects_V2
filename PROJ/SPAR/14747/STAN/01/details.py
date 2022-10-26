
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14747"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14747"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Pi AVR Programmer HAT')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Pi_AVR_Programmer_HAT')
    newPart['gitName'].append('SparkFun_Pi_AVR_Programmer_HAT')
    newPart['eagleBoard'].append('/HARDWARE/ADAPTER/SparkFun_Pi_AVR_Programmer_ADAPTER.brd')
    newPart['eagleSchem'].append('/HARDWARE/ADAPTER/SparkFun_Pi_AVR_Programmer_ADAPTER.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

