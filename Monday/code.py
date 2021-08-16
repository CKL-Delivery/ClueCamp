# Write your code here :-)
from adafruit_clue import clue

clue_data = clue.simple_text_display(title="CLUE Scavenger Hunt!", title_scale=2)

while True:
    clue_data[0].text = "Unlock the Sensors!"
    clue_data[1].text = "Spin right round"
    if clue.acceleration[0] > 10 or clue.acceleration[1] > 10 or clue.acceleration[0] > 10:
        clue_data[2].text = "Acceleration Sensor Completed!"

    clue_data[3].text = "Upside down"
    if clue.gyro[0] > 5 or clue.gyro[1] > 5 or clue.gyro[2] > 5:
        clue_data[4].text = "Gyroscope Sensor Completed!"

    clue_data[5].text = "Stay Cool"
    roomTemp = clue.temperature
    dropping_temp = roomTemp - 2
    if clue.temperature < dropping_temp:
        clue_data[6].text = "Temperature Sensor Completed"

    clue_data[7].text = "Opposites Attract"
    if clue.magnetic[0] > 50 or clue.magnetic[1] > 50 or clue.magnetic[2] > 50:
       clue_data[8].text = "Magnometer Sensor Completed!"

    clue_data[9].text = "Karaoke"
    if clue.sound_level > 250:
        clue_data[10].text = "Sound Sensor Completed!"

    clue_data[11].text = "Start of the alphabet"
    if clue.button_a:
        clue_data[12].text = "A Button Found"

    clue_data[13].text = "These love honey"
    if clue.button_b:
        clue_data[14].text = "B Button Found"

    clue_data[15].text = "All up in yo grill"
    if clue.proximity > 60:
        clue_data[16].text = "Proximity Sensor Complete"

    clue_data.show()
