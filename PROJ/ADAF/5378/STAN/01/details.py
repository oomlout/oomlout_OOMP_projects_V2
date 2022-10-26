
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5378"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5378"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit VEML7700 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-VEML7700-PCB')
    newPart['gitName'].append('Adafruit-VEML7700-PCB')
    newPart['eagleBoard'].append('/Adafruit VEML7700 STEMMA QT.brd')
    newPart['eagleSchem'].append('/Adafruit VEML7700 STEMMA QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

