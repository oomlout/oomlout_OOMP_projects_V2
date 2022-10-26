
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13230"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13230"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('HX711 Load Cell Amplifier')
    newPart['gitRepo'].append('https://github.com/sparkfun/HX711-Load-Cell-Amplifier')
    newPart['gitName'].append('HX711-Load-Cell-Amplifier')
    newPart['eagleBoard'].append('/hardware/SparkFun_HX711_Load_Cell.brd')
    newPart['eagleSchem'].append('/hardware/SparkFun_HX711_Load_Cell.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

