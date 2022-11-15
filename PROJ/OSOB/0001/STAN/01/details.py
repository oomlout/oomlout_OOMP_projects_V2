
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "OSOB"
    oColor = "0001"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0001"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Sensor watch')
    newPart['gitRepo'].append('https://github.com/joeycastillo/Sensor-Watch')
    newPart['gitName'].append('Sensor-Watch')
    newPart['eagleBoard'].append('PCB/ Main Boards/OSO-SWAT-A1-05.brd')
    newPart['eagleSchem'].append('PCB/ Main Boards/OSO-SWAT-A1-05.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

