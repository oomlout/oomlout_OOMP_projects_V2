
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18014"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18014"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic USB Hub USB2514B')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_USB_Hub-USB2514B')
    newPart['gitName'].append('Qwiic_USB_Hub-USB2514B')
    newPart['eagleBoard'].append('/Hardware/Qwiic-USB_Hub.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic-USB_Hub.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

