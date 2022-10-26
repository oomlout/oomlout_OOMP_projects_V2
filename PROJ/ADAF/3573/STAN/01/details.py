
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3573"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3573"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TPL5111 Reset Enable Timer PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TPL5111-Reset-Enable-Timer-PCB')
    newPart['gitName'].append('Adafruit-TPL5111-Reset-Enable-Timer-PCB')
    newPart['eagleBoard'].append('/Adafruit TPL5111 Reset Enable Timer.brd')
    newPart['eagleSchem'].append('/Adafruit TPL5111 Reset Enable Timer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

