
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3203"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3203"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Perma Proto Bonnet PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Perma-Proto-Bonnet-PCB')
    newPart['gitName'].append('Adafruit-Perma-Proto-Bonnet-PCB')
    newPart['eagleBoard'].append('/Adafruit Perma Proto Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit Perma Proto Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

