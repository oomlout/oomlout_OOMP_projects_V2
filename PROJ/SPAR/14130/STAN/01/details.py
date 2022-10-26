
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14130"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14130"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Roshamglo')
    newPart['gitRepo'].append('https://github.com/sparkfun/Roshamglo')
    newPart['gitName'].append('Roshamglo')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Roshamglo.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Roshamglo.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

