
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5625"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5625"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Qwiic Stemma QT 5 Port Hub PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Qwiic-Stemma-QT-5-Port-Hub-PCB')
    newPart['gitName'].append('Adafruit-Qwiic-Stemma-QT-5-Port-Hub-PCB')
    newPart['eagleBoard'].append('/Adafruit Stemma QT 5 Port Hub.brd')
    newPart['eagleSchem'].append('/Adafruit Stemma QT 5 Port Hub.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

