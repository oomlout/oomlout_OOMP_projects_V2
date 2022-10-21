
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15050"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15050"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Spectral Sensor AS7265x')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Spectral_Sensor_AS7265x')
    newPart['gitName'].append('Qwiic_Spectral_Sensor_AS7265x')
    newPart['eagleBoard'].append('/Hardware/Qwiic_Spectral_Sensor-AS7265x.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_Spectral_Sensor-AS7265x.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

