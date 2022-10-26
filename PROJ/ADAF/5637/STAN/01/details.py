
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5637"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5637"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit QT 5 3V Shifter PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-QT-5-3V-Shifter-PCB')
    newPart['gitName'].append('Adafruit-QT-5-3V-Shifter-PCB')
    newPart['eagleBoard'].append('/Adafruit QT 5-3V Shifter.brd')
    newPart['eagleSchem'].append('/Adafruit QT 5-3V Shifter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

