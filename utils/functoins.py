def color_picker(people):
    if people < 300000:
        return 'green'
    elif 300000 <= people < 600000:
        return 'orange'

    return 'red'


def change_radius(people):
    if people < 300000:
        return 8
    elif 300000 <= people < 600000:
        return 10

    return 14