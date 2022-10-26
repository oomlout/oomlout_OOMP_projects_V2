
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5189"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5189"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PCF8523 RTC Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PCF8523-RTC-Breakout-PCB')
    newPart['gitName'].append('Adafruit-PCF8523-RTC-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafrruit PCF8523 QT.brd')
    newPart['eagleSchem'].append('/Adafrruit PCF8523 QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

