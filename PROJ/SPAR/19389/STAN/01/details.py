
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "19389"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR19389"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Analog MEMS Microphone Breakout SPH8878LR5H 1')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Analog_MEMS_Microphone_Breakout_SPH8878LR5H-1')
    newPart['gitName'].append('SparkFun_Analog_MEMS_Microphone_Breakout_SPH8878LR5H-1')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Analog_MEMS_Microphone_Breakout_SPH8878LR5H-1.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Analog_MEMS_Microphone_Breakout_SPH8878LR5H-1.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

