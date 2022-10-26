
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5394"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5394"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 1.9in 320x170 Color IPS TFT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-1.9in-320x170-Color-IPS-TFT-PCB')
    newPart['gitName'].append('Adafruit-1.9in-320x170-Color-IPS-TFT-PCB')
    newPart['eagleBoard'].append('/Adafruit 1.9in 320x170 Color IPS TFT.brd')
    newPart['eagleSchem'].append('/Adafruit 1.9in 320x170 Color IPS TFT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

