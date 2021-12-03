from datetime import datetime

SUNRISE = datetime.strptime('06:00', '%H:%M')
SUNSET = datetime.strptime('18:00', '%H:%M')


def sun_angle(time, sunrise=SUNRISE, sunset=SUNSET):
    time = datetime.strptime(time, '%H:%M')
    if not sunrise <= time <= sunset:
        return "I don't see the sun!"

    angle_per_hour = 180 / (sunset - sunrise).seconds * 3600
    time_since_sunrise = (time - sunrise).seconds / 3600
    return time_since_sunrise * angle_per_hour


if __name__ == "__main__":
 x = input("Please enter time in format HH:MM:\n")

 output = sun_angle(x)

 print(f'In {x} sun angle will be {output}\n')

