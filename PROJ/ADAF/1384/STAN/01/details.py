
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1384"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1384"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit GA1A1S202WP Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-GA1A1S202WP-Breakout-PCB')
    newPart['gitName'].append('Adafruit-GA1A1S202WP-Breakout-PCB')
    newPart['eagleBoard'].append('/GA1A1S202WP-REV-B.brd')
    newPart['eagleSchem'].append('/GA1A1S202WP-REV-B.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

