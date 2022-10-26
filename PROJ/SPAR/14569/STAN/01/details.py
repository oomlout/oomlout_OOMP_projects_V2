
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14569"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14569"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic NonContact Thermo MLX90632')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_NonContact_Thermo_MLX90632')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_NonContact_Thermo_MLX90632')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_NonContact_Thermo_MLX90632/Hardware/Qwiic_NonContact_Thermo_MLX90632.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_NonContact_Thermo_MLX90632/Hardware/Qwiic_NonContact_Thermo_MLX90632.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

