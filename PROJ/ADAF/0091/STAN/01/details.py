
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0091"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0091"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit USB Boarduino PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_USB_Boarduino_PCB')
    newPart['gitName'].append('Adafruit_USB_Boarduino_PCB')
    newPart['eagleBoard'].append('/usbboarduino20.brd')
    newPart['eagleSchem'].append('/usbboarduino20.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

