
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14347"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14347"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Spectral Sensor AS726X')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Spectral_Sensor_AS726X')
    newPart['gitName'].append('Qwiic_Spectral_Sensor_AS726X')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Spectral_Sensor-AS726x.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Spectral_Sensor-AS726x.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

