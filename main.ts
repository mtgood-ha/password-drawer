let password = 0
let input_number = 0
basic.showIcon(IconNames.Heart)
pins.setPull(DigitalPin.P1, PinPullMode.PullUp)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("reset")
    show_number()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    password = input_number
    basic.showString("set")
    basic.clearScreen()
    basic.pause(500)
})
forever(function on_forever() {
    
    if (pins.analogReadPin(AnalogPin.P0) < 100) {
        input_number = 0
    } else if (pins.analogReadPin(AnalogPin.P0) < 200) {
        input_number = 1
    } else if (pins.analogReadPin(AnalogPin.P0) < 300) {
        input_number = 2
    } else if (pins.analogReadPin(AnalogPin.P0) < 400) {
        input_number = 3
    } else if (pins.analogReadPin(AnalogPin.P0) < 500) {
        input_number = 4
    } else if (pins.analogReadPin(AnalogPin.P0) < 600) {
        input_number = 5
    } else if (pins.analogReadPin(AnalogPin.P0) < 700) {
        input_number = 6
    } else if (pins.analogReadPin(AnalogPin.P0) < 800) {
        input_number = 7
    } else if (pins.analogReadPin(AnalogPin.P0) < 875) {
        input_number = 8
    } else if (pins.analogReadPin(AnalogPin.P0) < 1024) {
        input_number = 9
    }
    
})
function show_number() {
    loops.everyInterval(500, function onEvery_interval() {
        basic.showNumber(input_number)
    })
}

input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    if (password == input_number) {
        wuKong.setMotorSpeed(wuKong.MotorList.M1, 20)
        basic.pause(250)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, 0)
    }
    
    if (password != input_number) {
        pins.digitalWritePin(DigitalPin.P2, 1)
        basic.pause(500)
        pins.digitalWritePin(DigitalPin.P2, 0)
    }
    
})
