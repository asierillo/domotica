
from microbit import*
import music

pir = pin15

while True:
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
  else:
  for lo que quieras poner in range(5):
  np[0] = (0, 0, 0)
  np[1] = (0, 0, 0)
  np.show()
  led.write_digital(0)
  sleep(100)
