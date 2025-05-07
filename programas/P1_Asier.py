
from microbit import*
import music

pir = pin15.read_digital()
np = neopixel.NeoPixel(pin13)
led = pin14

while True:
  if pir ==1:
    music.play(music.RINGTONE)
  if pir.read_digital():
    music.play(music.RINGTONE)
    sleep(100)
    music.play(music.RINGTONE)
    sleep(500)
    for lo q quieras poner in range(5):
    np[0] = (0, 255, 0)
    np[1] = (0, 255, 0)
    np.show()
    led.write_digital(1)
    sleep(100)
     led.write_digital(0)
  sleep(100)
  led.write_digital(1)
  sleep(500)
  led.write_digital(0)
  else:
  for lo que quieras poner in range(5):
  np[0] = (0, 0, 0)
  np[1] = (0, 0, 0)
  np.show()
  led.write_digital(0)
  sleep(100)
  led.write_digital(1)
  sleep(500)
  led.write_digital(0)
  np.clear
display.show(Image.ANGRY)
display.clear
