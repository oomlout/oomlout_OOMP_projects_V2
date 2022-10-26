
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3015"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3015"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PiGRRL PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PiGRRL-PCB')
    newPart['gitName'].append('Adafruit-PiGRRL-PCB')
    newPart['eagleBoard'].append('/PiGRRL-ButtonPCB.brd')
    newPart['eagleSchem'].append('/PiGRRL-ButtonPCB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

