import random


def get_custom_values():
    speed_values = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 60]
    rpm_values = [1200, 2500, 4500, 4500, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 2000]
    current_speed = 60

    for i in range(0, 30):
        speed_to_add = current_speed + random.choice(range(-3, 3, 1))
        if speed_to_add < 50:
            speed_to_add = 53
        if speed_to_add > 70:
            speed_to_add = 67
        if speed_to_add < current_speed:
            current_rpm = 2000
        else:
            current_rpm = 4000
        speed_values.append(speed_to_add)
        rpm_values.append(current_rpm)

    for value in reversed(speed_values):
        speed_values.append(value)
    for value in reversed(rpm_values):
        rpm_values.append(value)

    return speed_values, rpm_values


def mph_to_kph(mph):
    return round(mph * 1.60934)


def construct_rpm(rpm_value):
    return_value = f'{rpm_value:04X}'
    return return_value
