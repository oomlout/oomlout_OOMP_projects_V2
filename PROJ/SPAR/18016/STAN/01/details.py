
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

    newPart['name'].append('USB Current Sensor')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB_Current_Sensor')
    newPart['gitName'].append('USB_Current_Sensor')
    newPart['eagleBoard'].append('/Hardware/USB_Current_Sensor.brd')
    newPart['eagleSchem'].append('/Hardware/USB_Current_Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

