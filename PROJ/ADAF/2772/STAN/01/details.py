
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2772"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2772"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Feather M0 Basic Proto PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Feather-M0-Basic-Proto-PCB')
    newPart['gitName'].append('Adafruit-Feather-M0-Basic-Proto-PCB')
    newPart['eagleBoard'].append('/Adafruit Feather M0 Basic rev C.brd')
    newPart['eagleSchem'].append('/Adafruit Feather M0 Basic rev C.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

