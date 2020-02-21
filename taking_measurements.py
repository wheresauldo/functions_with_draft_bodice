bodice_measurement = ['nape_to_waist', 'armhole_height', 'full_bust', 'waist_circumference', 'bust_height',
'neck_circumference', 'shoulder_length']

master_sloper_dict = {
    }

your_sloper_dict = {
    }

def take_measurements():
        measurements = []
        measurements_profile = input("Your name ")
        for variable in bodice_measurement:
            measurements.append(input(variable + " "))
            for measurement in measurements:
                your_sloper_dict.update({variable : measurement})
                master_sloper_dict.update({measurements_profile: your_sloper_dict})
        print(master_sloper_dict)

take_measurements()
