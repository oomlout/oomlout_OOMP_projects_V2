
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5020"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5020"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoKey Trinkey PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoKey-Trinkey-PCB')
    newPart['gitName'].append('Adafruit-NeoKey-Trinkey-PCB')
    newPart['eagleBoard'].append('/Adafruit NeoKey Trinkey.brd')
    newPart['eagleSchem'].append('/Adafruit NeoKey Trinkey.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

