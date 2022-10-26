
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0495"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0495"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SOIC20 DIP Adapter')
    newPart['gitRepo'].append('https://github.com/sparkfun/SOIC20-DIP_Adapter')
    newPart['gitName'].append('SOIC20-DIP_Adapter')
    newPart['eagleBoard'].append('/Hardware/SparkFun_SOIC20_Adapter_v10.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_SOIC20_Adapter_v10.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

