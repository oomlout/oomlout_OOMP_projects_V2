
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9814"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9814"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ADXL345 Eval')
    newPart['gitRepo'].append('https://github.com/sparkfun/ADXL345_Eval')
    newPart['gitName'].append('ADXL345_Eval')
    newPart['eagleBoard'].append('/hardware/ADXL345_Eval_Board-v11.brd')
    newPart['eagleSchem'].append('/hardware/ADXL345_Eval_Board-v11.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

