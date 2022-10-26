
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2566"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2566"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Flora Sewable 3 Pin JST Wiring Adapter PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Flora-Sewable-3-Pin-JST-Wiring-Adapter-PCB')
    newPart['gitName'].append('Adafruit-Flora-Sewable-3-Pin-JST-Wiring-Adapter-PCB')
    newPart['eagleBoard'].append('/Adafruit Flora 3JST.brd')
    newPart['eagleSchem'].append('/Adafruit Flora 3JST.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

