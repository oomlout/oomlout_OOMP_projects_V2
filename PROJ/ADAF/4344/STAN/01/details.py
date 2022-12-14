
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4344"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4344"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MSA301 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-MSA301-PCB')
    newPart['gitName'].append('Adafruit-MSA301-PCB')
    newPart['eagleBoard'].append('/Adafruit MSA301.brd')
    newPart['eagleSchem'].append('/Adafruit MSA301.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

