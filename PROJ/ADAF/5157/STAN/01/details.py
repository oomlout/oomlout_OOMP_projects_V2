
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5157"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5157"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoKey Snap Apart PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoKey-Snap-Apart-PCB')
    newPart['gitName'].append('Adafruit-NeoKey-Snap-Apart-PCB')
    newPart['eagleBoard'].append('/NeoKey 5x6 Ortho Snap-Apart.brd')
    newPart['eagleSchem'].append('/NeoKey 5x6 Ortho Snap-Apart.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

