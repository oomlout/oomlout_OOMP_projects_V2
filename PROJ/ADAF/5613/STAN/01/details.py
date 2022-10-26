
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5613"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5613"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit EYESPI PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-EYESPI-PCB')
    newPart['gitName'].append('Adafruit-EYESPI-PCB')
    newPart['eagleBoard'].append('/Adafruit EYESPI Breakout Board.brd')
    newPart['eagleSchem'].append('/Adafruit EYESPI Breakout Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

