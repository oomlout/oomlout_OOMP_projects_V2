
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18632"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18632"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Environmental Sensor Function Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Environmental_Sensor_Function_Board')
    newPart['gitName'].append('MicroMod_Environmental_Sensor_Function_Board')
    newPart['eagleBoard'].append('/Hardware/MicroMod_Environmental.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod_Environmental.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

