
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3678"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3678"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit UDA1334A I2S Stereo DAC PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-UDA1334A-I2S-Stereo-DAC-PCB')
    newPart['gitName'].append('Adafruit-UDA1334A-I2S-Stereo-DAC-PCB')
    newPart['eagleBoard'].append('/Adafruit UDA1334 I2S DAC.brd')
    newPart['eagleSchem'].append('/Adafruit UDA1334 I2S DAC.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

