
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4632"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4632"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PMSA003I PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PMSA003I-PCB')
    newPart['gitName'].append('Adafruit-PMSA003I-PCB')
    newPart['eagleBoard'].append('/Adafruit PMSA003I.brd')
    newPart['eagleSchem'].append('/Adafruit PMSA003I.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

