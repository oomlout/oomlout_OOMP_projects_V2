
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5640"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5640"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Si5351A Clock Generator with STEMMA QT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Si5351A-Clock-Generator-with-STEMMA-QT-PCB')
    newPart['gitName'].append('Adafruit-Si5351A-Clock-Generator-with-STEMMA-QT-PCB')
    newPart['eagleBoard'].append('/Si5351 STEMMA QT Board.brd')
    newPart['eagleSchem'].append('/Si5351 STEMMA QT Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

