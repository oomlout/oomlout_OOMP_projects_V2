
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3988"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3988"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Prop Maker FeatherWing PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Prop-Maker-FeatherWing-PCB')
    newPart['gitName'].append('Adafruit-Prop-Maker-FeatherWing-PCB')
    newPart['eagleBoard'].append('/Adafruit Prop Maker FeatherWing.brd')
    newPart['eagleSchem'].append('/Adafruit Prop Maker FeatherWing.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

