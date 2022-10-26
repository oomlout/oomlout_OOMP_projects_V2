
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "10740"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR10740"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('IR Thermometer Evaluation Board MLX90614')
    newPart['gitRepo'].append('https://github.com/sparkfun/IR_Thermometer_Evaluation_Board-MLX90614')
    newPart['gitName'].append('IR_Thermometer_Evaluation_Board-MLX90614')
    newPart['eagleBoard'].append('/Hardware/SparkFun_IR_Thermometer_Eval-MLX90614.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_IR_Thermometer_Eval-MLX90614.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

