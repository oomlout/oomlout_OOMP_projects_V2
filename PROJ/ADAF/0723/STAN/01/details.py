
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0723"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0723"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Perma Proto PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Perma-Proto-PCB')
    newPart['gitName'].append('Adafruit-Perma-Proto-PCB')
    newPart['eagleBoard'].append('/adafruit minty permaproto.brd')
    newPart['eagleSchem'].append('/adafruit minty permaproto.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

