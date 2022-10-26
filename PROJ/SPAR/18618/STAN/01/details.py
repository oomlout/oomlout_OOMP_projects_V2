
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18618"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18618"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/SparkX smol ARTIC R2')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/SparkX_smol_ARTIC_R2')
    newPart['gitName'].append('https://github.com/sparkfunX/SparkX_smol_ARTIC_R2')
    newPart['eagleBoard'].append('sourceFiles/git/SparkX_smol_ARTIC_R2/Hardware/SparkX_smol_ARTIC_R2.brd')
    newPart['eagleSchem'].append('sourceFiles/git/SparkX_smol_ARTIC_R2/Hardware/SparkX_smol_ARTIC_R2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

