
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4534"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4534"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Bonsai Buckaroo PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Bonsai-Buckaroo-PCB')
    newPart['gitName'].append('Adafruit-Bonsai-Buckaroo-PCB')
    newPart['eagleBoard'].append('/Adafruit Bonsai Buckaroo.brd')
    newPart['eagleSchem'].append('/Adafruit Bonsai Buckaroo.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

