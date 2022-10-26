
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1222"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1222"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Gemma PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Gemma-PCB')
    newPart['gitName'].append('Adafruit-Gemma-PCB')
    newPart['eagleBoard'].append('/Adafruit Gemma rev B.brd')
    newPart['eagleSchem'].append('/Adafruit Gemma rev B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

