
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "0494"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0494"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SOIC8 DIP Adapter')
    newPart['gitRepo'].append('https://github.com/sparkfun/SOIC8-DIP_Adapter')
    newPart['gitName'].append('SOIC8-DIP_Adapter')
    newPart['eagleBoard'].append('/Documentation/SparkFun_SOIC8-DIP-Adapter-Dimensions.brd')
    newPart['eagleSchem'].append('/Documentation/SparkFun_SOIC8-DIP-Adapter-Dimensions.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

