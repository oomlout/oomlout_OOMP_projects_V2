
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13830"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13830"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('USB UART Serial Breakout CY7C65213')
    newPart['gitRepo'].append('https://github.com/sparkfun/USB_UART_Serial_Breakout-CY7C65213')
    newPart['gitName'].append('USB_UART_Serial_Breakout-CY7C65213')
    newPart['eagleBoard'].append('/Hardware/SparkFun_Cypress_USBUART_BOB.brd')
    newPart['eagleSchem'].append('/Hardware/SparkFun_Cypress_USBUART_BOB.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

