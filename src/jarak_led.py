import RPi.GPIO as GPIO
import time

# Setup mode GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Definisikan pin
TRIG = 23
ECHO = 24
LED = 8

# Setup pin
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def get_distance():
    # Kirim sinyal TRIG
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Tunggu ECHO mulai
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    # Tunggu ECHO selesai
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    # Hitung durasi pulse
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Kecepatan suara
    distance = round(distance, 2)
    
    return distance

try:
    while True:
        dist = get_distance()
        print(f"Jarak: {dist} cm")
        
        if dist < 20:
            GPIO.output(LED, GPIO.HIGH)  # Nyalakan LED
        else:
            GPIO.output(LED, GPIO.LOW)   # Matikan LED
        
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Dihentikan oleh pengguna")
    GPIO.cleanup()