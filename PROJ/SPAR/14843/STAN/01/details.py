
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14843"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14843"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/Qwiic IR Array MLX90640')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/Qwiic_IR_Array_MLX90640')
    newPart['gitName'].append('https://github.com/sparkfunX/Qwiic_IR_Array_MLX90640')
    newPart['eagleBoard'].append('sourceFiles/git/Qwiic_IR_Array_MLX90640/Hardware/sparkfun-mlx90640-qwiic-breakout.brd')
    newPart['eagleSchem'].append('sourceFiles/git/Qwiic_IR_Array_MLX90640/Hardware/sparkfun-mlx90640-qwiic-breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

