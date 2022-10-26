
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18731"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18731"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/SparkX smol FPC 16 way 36mm')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/SparkX_smol_FPC_16-way_36mm')
    newPart['gitName'].append('https://github.com/sparkfunX/SparkX_smol_FPC_16-way_36mm')
    newPart['eagleBoard'].append('sourceFiles/git/SparkX_smol_FPC_16-way_36mm/Hardware/16_POS_0_5MM_PITCH_36MM_LENGTH.brd')
    newPart['eagleSchem'].append('sourceFiles/git/SparkX_smol_FPC_16-way_36mm/Hardware/16_POS_0_5MM_PITCH_36MM_LENGTH.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

