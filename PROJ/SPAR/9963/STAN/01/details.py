
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "9963"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR9963"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RFID USB Reader')
    newPart['gitRepo'].append('https://github.com/sparkfun/RFID_USB_Reader')
    newPart['gitName'].append('RFID_USB_Reader')
    newPart['eagleBoard'].append('/Hardware/RFID_USB_Reader-v18.brd')
    newPart['eagleSchem'].append('/Hardware/RFID_USB_Reader-v18.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

