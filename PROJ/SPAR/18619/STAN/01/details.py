
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18619"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18619"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkX smol ESP32')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkX_smol_ESP32')
    newPart['gitName'].append('SparkX_smol_ESP32')
    newPart['eagleBoard'].append('/Hardware/SparkX_smol_ESP32.brd')
    newPart['eagleSchem'].append('/Hardware/SparkX_smol_ESP32.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

