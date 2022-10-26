
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13281"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13281"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Load Sensor Combinator')
    newPart['gitRepo'].append('https://github.com/sparkfun/Load_Sensor_Combinator')
    newPart['gitName'].append('Load_Sensor_Combinator')
    newPart['eagleBoard'].append('/Hardware/SparkFun Load Sensor Combinator.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun Load Sensor Combinator.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

