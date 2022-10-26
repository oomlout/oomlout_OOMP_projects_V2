
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18016"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18016"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('https://github.com/sparkfunX/USB Current Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/https://github.com/sparkfunX/USB_Current_Sensor')
    newPart['gitName'].append('https://github.com/sparkfunX/USB_Current_Sensor')
    newPart['eagleBoard'].append('sourceFiles/git/USB_Current_Sensor/Hardware/USB_Current_Sensor.brd')
    newPart['eagleSchem'].append('sourceFiles/git/USB_Current_Sensor/Hardware/USB_Current_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

