# Define state variables
count = 0  # variable to keep track of time in seconds
state = "red"  # initial state of the traffic light
pedestrian_present = False  # initial state of the pedestrian input

# Define output variables
sigG = False  # output to turn on the green light
sigY = False  # output to change the light to yellow
sigR = True  # output to change the light to red

# Simulate the traffic light for 200 seconds
for i in range(200):
    count += 1  # increment time count

    # check for input from pedestrian
    if count == 70:
        pedestrian_present = True
        print(f"Second {i+1}: Pedestrian input = {pedestrian_present}")
    else:
        pedestrian_present = False

    # Update state of traffic light based on current state and input
    if state == "red":
        if count == 60:
            state = "green"
            count = 0
        sigG = False
        sigY = False
        sigR = True

    elif state == "green":
        if pedestrian_present:
            if count >= 60:
                state = "yellow"
                count = 0
            else:
                state = "pending"
            sigG = False
            sigY = False
            sigR = True
        else:
            sigG = True
            sigY = False
            sigR = False

    elif state == "pending":
        if count == 60:
            state = "yellow"
            count = 0
        sigG = False
        sigY = False
        sigR = True

    elif state == "yellow":
        if count == 5:
            state = "red"
            count = 0
        sigG = False
        sigY = True
        sigR = False

    # Print output for the current second
    print(f"Second {i+1}: State = {state}, SigG = {sigG}, SigY = {sigY}, SigR = {sigR}")


