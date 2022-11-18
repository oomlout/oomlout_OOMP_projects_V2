
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17874"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17874"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Differential Pressure Sensor SDP31')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Differential_Pressure_Sensor-SDP31')
    newPart['gitName'].append('Qwiic_Differential_Pressure_Sensor-SDP31')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Differential_Pressure_Sensor-SDP31.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Differential_Pressure_Sensor-SDP31.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

