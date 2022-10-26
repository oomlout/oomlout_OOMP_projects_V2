
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5302"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5302"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit KB2040 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-KB2040-PCB')
    newPart['gitName'].append('Adafruit-KB2040-PCB')
    newPart['eagleBoard'].append('/Adafruit KB2040.brd')
    newPart['eagleSchem'].append('/Adafruit KB2040.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

