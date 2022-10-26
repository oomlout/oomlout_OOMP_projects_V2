
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18620"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18620"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/SparkX smol Header')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/SparkX_smol_Header')
    newPart['gitName'].append('https://github.com/sparkfunX/SparkX_smol_Header')
    newPart['eagleBoard'].append('sourceFiles/git/SparkX_smol_Header/Hardware/SparkX_smol_Header.brd')
    newPart['eagleSchem'].append('sourceFiles/git/SparkX_smol_Header/Hardware/SparkX_smol_Header.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

