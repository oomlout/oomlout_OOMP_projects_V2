
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14289"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14289"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic Human Presence Sensor AK9750')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_Human_Presence_Sensor-AK9750')
    newPart['gitName'].append('Qwiic_Human_Presence_Sensor-AK9750')
    newPart['eagleBoard'].append('/Hardware/AK9750 Human Movement Sensor Breakout.brd')
    newPart['eagleSchem'].append('/Hardware/AK9750 Human Movement Sensor Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

