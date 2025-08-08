password = 0
input_number = 0
basic.show_icon(IconNames.HEART)
pins.set_pull(DigitalPin.P1, PinPullMode.PULL_UP)


def on_button_pressed_a():
    basic.show_string("reset")
    show_number()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global password
    password = input_number
    basic.show_string("set")
    basic.clear_screen()
    basic.pause(500)
input.on_button_pressed(Button.B, on_button_pressed_b)
    
def on_forever():
    global input_number
    if pins.analog_read_pin(AnalogPin.P0) < 100:
        input_number = 0
    elif pins.analog_read_pin(AnalogPin.P0) < 200:
        input_number = 1
    elif pins.analog_read_pin(AnalogPin.P0) < 300:
        input_number = 2
    elif pins.analog_read_pin(AnalogPin.P0) < 400:
        input_number = 3
    elif pins.analog_read_pin(AnalogPin.P0) < 500:
        input_number = 4
    elif pins.analog_read_pin(AnalogPin.P0) < 600:
        input_number = 5
    elif pins.analog_read_pin(AnalogPin.P0) < 700:
        input_number = 6
    elif pins.analog_read_pin(AnalogPin.P0) < 800:
        input_number = 7
    elif pins.analog_read_pin(AnalogPin.P0) < 875:
        input_number = 8
    elif pins.analog_read_pin(AnalogPin.P0) < 1024:
        input_number = 9
forever(on_forever)

def show_number():
    def onEvery_interval():
        basic.show_number(input_number)
    loops.every_interval(500, onEvery_interval)

def on_pin_pressed_p1():
    if password == input_number:
        wuKong.set_motor_speed(wuKong.MotorList.M1, 20)
        basic.pause(250)
        wuKong.set_motor_speed(wuKong.MotorList.M1, 0)
    if password != input_number:
        pins.digital_write_pin(DigitalPin.P2, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P2, 0)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
