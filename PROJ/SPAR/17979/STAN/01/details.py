
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17979"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17979"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Sound Trigger')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Sound_Trigger')
    newPart['gitName'].append('Qwiic_Sound_Trigger')
    newPart['eagleBoard'].append('/Hardware/Qwiic Sound Trigger.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic Sound Trigger.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

