
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "8464"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR8464"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad Light Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/LilyPad_Light_Sensor')
    newPart['gitName'].append('LilyPad_Light_Sensor')
    newPart['eagleBoard'].append('/Hardware/LilyPad_Light_Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/LilyPad_Light_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

