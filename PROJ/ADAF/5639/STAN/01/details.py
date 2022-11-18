
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5639"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5639"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit High Power Infrared LED Emitter PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-High-Power-Infrared-LED-Emitter-PCB')
    newPart['gitName'].append('Adafruit-High-Power-Infrared-LED-Emitter-PCB')
    newPart['eagleBoard'].append('/IR STEMMA LED Emitter.brd')
    newPart['eagleSchem'].append('/IR STEMMA LED Emitter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

