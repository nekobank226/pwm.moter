import pigpio
import time
import Adafruit_PCA9685

#設定周波数
SET_FREQ = 50

#ピンの設定
pi = pigpio.pi()
pi.set_mode(14,pigpio.OUTPUT)
pi.set_mode(15,pigpio.OUTPUT)

#PCA9685の初期化
PCA9685 = Adafruit_PCA9685.PCA9685()
PCA9685.set_pwm_freq(SET_FREQ)

#時計回りに回転
pi.write(14,1)
pi.write(15,0)
PCA9685.set_pwm(0,0,1000)
time.sleep(2)
#回転速度を早く
pi.write(14,1)
pi.write(15,0)
PCA9685.set_pwm(0,0,2000)
time.sleep(2)

#逆回転
pi.write(14,0)
pi.write(15,1)
PCA9685.set_pwm(0,0,1000)
time.sleep(2)
#回転速度を早く
pi.write(14,0)
pi.write(15,1)
PCA9685.set_pwm(0,0,2000)
time.sleep(2)

