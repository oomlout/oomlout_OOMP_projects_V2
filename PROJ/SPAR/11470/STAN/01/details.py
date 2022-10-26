
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "11470"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR11470"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qtechknow ArduSensor Learning Kit')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qtechknow_ArduSensor_Learning_Kit')
    newPart['gitName'].append('Qtechknow_ArduSensor_Learning_Kit')
    newPart['eagleBoard'].append('/ArduSensor PCB/Hardware/SensorBoard-v11.brd')
    newPart['eagleSchem'].append('/ArduSensor PCB/Hardware/SensorBoard-v11.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

