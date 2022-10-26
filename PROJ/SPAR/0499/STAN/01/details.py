
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0499"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0499"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SSOP DIP Adapter 20 Pin')
    newPart['gitRepo'].append('https://github.com/sparkfun/SSOP-DIP_Adapter_20-Pin')
    newPart['gitName'].append('SSOP-DIP_Adapter_20-Pin')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Adapter-SSOP20-v10.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Adapter-SSOP20-v10.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

