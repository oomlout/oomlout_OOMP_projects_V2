
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2077"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2077"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Proto Shield PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Proto-Shield-PCB')
    newPart['gitName'].append('Adafruit-Proto-Shield-PCB')
    newPart['eagleBoard'].append('/Adafruit Proto Shield.brd')
    newPart['eagleSchem'].append('/Adafruit Proto Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

