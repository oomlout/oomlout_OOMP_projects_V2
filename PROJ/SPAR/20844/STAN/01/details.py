
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "20844"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR20844"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Indoor Air Quality Sensor ENS160')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Indoor_Air_Quality_Sensor-ENS160')
    newPart['gitName'].append('SparkFun_Indoor_Air_Quality_Sensor-ENS160')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Air_Quality_ENS160.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Air_Quality_ENS160.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

