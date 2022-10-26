
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5022"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5022"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Proximity Trinkey PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Proximity-Trinkey-PCB')
    newPart['gitName'].append('Adafruit-Proximity-Trinkey-PCB')
    newPart['eagleBoard'].append('/Adafruit Proximity Trinkey.brd')
    newPart['eagleSchem'].append('/Adafruit Proximity Trinkey.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

