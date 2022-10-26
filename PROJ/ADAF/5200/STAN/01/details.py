
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5200"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5200"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Proto PiCowbell PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Proto-PiCowbell-PCB')
    newPart['gitName'].append('Adafruit-Proto-PiCowbell-PCB')
    newPart['eagleBoard'].append('/Adafruit Proto PiCowbell.brd')
    newPart['eagleSchem'].append('/Adafruit Proto PiCowbell.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

