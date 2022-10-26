
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4000"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4000"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Metro M4 Express AirLift PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Metro-M4-Express-AirLift-PCB')
    newPart['gitName'].append('Adafruit-Metro-M4-Express-AirLift-PCB')
    newPart['eagleBoard'].append('/Metro M4 Express AirLift.brd')
    newPart['eagleSchem'].append('/Metro M4 Express AirLift.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

