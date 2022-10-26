
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2741"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2741"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Pixie 3W Smart LED PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Pixie-3W-Smart-LED-PCB')
    newPart['gitName'].append('Pixie-3W-Smart-LED-PCB')
    newPart['eagleBoard'].append('/Pixie.brd')
    newPart['eagleSchem'].append('/Pixie.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

