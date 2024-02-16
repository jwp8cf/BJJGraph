transitions = [  # transitions Techniques
    {"name": 'Deep Half Guard', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    {"name": 'Guard-to-Mount', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    # Takedown Transitions
    {"name": 'Single Leg Takedown', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    {"name": 'Double Leg Takedown', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    # Sweep Transitions
    # Sweep Transitions
    {"name": 'Scissor Sweep', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    {"name": 'Flower Sweep', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    {"name": 'Hip Bump Sweep', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    {"name": 'Pendulum Sweep', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    {"name": 'Elevator Sweep', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    # Passing Techniques
    {"name": 'Toreando Pass', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    {"name": 'Double Under Pass', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    {"name": 'Over Under Pass', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    {"name": 'Leg Drag Pass', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    {"name": 'X-Pass', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},
    #butterfly sweep
    {"name": 'Butterfly Sweep', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition'},

    {"name": 'Stack Defense', "difficulty": 'Medium', "beltLevel": 'Blue', "type": 'Control'},
    {"name": 'Cross Face', "difficulty": 'Medium', "beltLevel": 'Blue', "type": 'Control'},
    {"name": 'Scooping', "difficulty": 'Medium', "beltLevel": 'Blue', "type": 'Control'},
    #technical stand up
    {"name": 'Technical Stand Up', "difficulty": 'Low', "beltLevel": 'White', "type": 'Transition', 'image': 'public/images/transitions/technical-standup.jpg'},
    #fireman's carry
    {"name": 'Fireman\'s Carry', "difficulty": 'Medium', "beltLevel": 'Blue', "type": 'Transition', 'image': 'public/images/transitions/firemans-carry.jpg'},
    #duplex
    {"name": 'Duplex', "difficulty": 'Medium', "beltLevel": 'Blue', "type": 'Transition', 'image': 'public/images/transitions/duplex.png'},
]


transitions_leading_to_position =  [
    {"transition": 'Scissor Sweep', "position2": 'Seated Mount (top)'},
    {"transition": 'Flower Sweep', "position2": 'Seated Mount (top)'},
    {"transition": 'Hip Bump Sweep', "position2": 'Seated Mount (top)'},
    {"transition": 'Double Leg Takedown',  "position2": 'Side Control (top)'},
    {"transition": 'Double Leg Takedown', "position2": 'Half Guard (top)'},
    {"transition": 'Single Leg Takedown', "position2": 'Half Guard (top)'},
    {"transition": 'Single Leg Takedown', "position2": 'Side Control (top)'},

    #butterfly sweep to mount
    {"transition": 'Butterfly Sweep', "position2": 'Seated Mount (top)'},
    # single leg from shin on shin to Side Control (top)
    {"transition": 'Single Leg Takedown', "position2": 'Back Control (take)'},
]