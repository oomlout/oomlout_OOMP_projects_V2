
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13158"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13158"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LiPower Shield')
    newPart['gitRepo'].append('https://github.com/sparkfun/LiPower-Shield')
    newPart['gitName'].append('LiPower-Shield')
    newPart['eagleBoard'].append('/Hardware/SparkFunLiPowerShield.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFunLiPowerShield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

