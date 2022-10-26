
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4530"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4530"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LPS2X PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LPS2X-PCB')
    newPart['gitName'].append('Adafruit-LPS2X-PCB')
    newPart['eagleBoard'].append('/Adafruit-LPS22-Rev-A.brd')
    newPart['eagleSchem'].append('/Adafruit-LPS22-Rev-A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

