
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3531"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3531"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit 128x64 OLED Bonnet for Raspberry Pi PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-128x64-OLED-Bonnet-for-Raspberry-Pi-PCB')
    newPart['gitName'].append('Adafruit-128x64-OLED-Bonnet-for-Raspberry-Pi-PCB')
    newPart['eagleBoard'].append('/Adafruit 128x64 OLED Bonnet.brd')
    newPart['eagleSchem'].append('/Adafruit 128x64 OLED Bonnet.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

