
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3421"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3421"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit I2S Microphone Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-I2S-Microphone-Breakout-PCB')
    newPart['gitName'].append('Adafruit-I2S-Microphone-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit I2S Mic SPK0415HM4H.brd')
    newPart['eagleSchem'].append('/Adafruit I2S Mic SPK0415HM4H.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

