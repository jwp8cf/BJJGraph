positions = [
    {"name": 'Open Guard (top)', "image": "/images/positions/open-guard.webp"},
    {"name": 'Open Guard (bottom)', "image": "/images/positions/open-guard.webp"},
    {"name": 'Closed Guard (top)', "image": "/images/positions/Closed_guard.png"},
    {"name": 'Closed Guard (bottom)', "image": "/images/positions/Closed_guard.png"},
    {"name": 'Side Control (top)', "image": "/images/positions/Side-Control.png"},
    {"name": 'Side Control (bottom)', "image": "/images/positions/Side-Control.png"},
    # {"name": 'Butterfly Guard (top)', "image": "/images/positions/Butterfly-Guard.png"},
    {"name": 'Butterfly Guard (bottom)', "image": "/images/positions/Butterfly-Guard.png"},
    {"name": 'Seated Mount (top)', "image": "/images/positions/Mount.png"},
    # {"name": 'Seated Mount (bottom)', "image": "/images/positions/Mount.png"},
    {"name": 'Knee on Belly (top)', "image": "/images/positions/Knee-on-Belly.png"},
    # {"name": 'Knee on Belly (bottom)', "image": "/images/positions/Knee-on-Belly.png"},
    {"name": 'Turtle (top)', "image": "/images/positions/Turtle.png"},
    {"name": 'Turtle (bottom)', "image": "/images/positions/Turtle.png"},
    {"name": 'North-South (top)', "image": "/images/positions/North-South.png"},
    # {"name": 'North-South (bottom)', "image": "/images/positions/North-South.png"},
    {"name": 'Half Guard (top)', "image": "/images/positions/half-guard.png"},
    {"name": 'Half Guard (bottom)', "image": "/images/positions/half-guard.png"},
    {"name": 'Back Control (take)', "image": "/images/positions/Back-Mount.png"},
    {"name": 'Back Control (taken)', "image": "/images/positions/Back-Mount.png"},
    {"name": 'Truck (take)', "image": "/images/positions/the-truck.jpg"},
    # {"name": 'Truck (taken)', "image": "/images/positions/the-truck.jpg"},
    # {"name": 'Lasso Guard (top)', "gi": "true", "image": "/images/positions/Lasso.png"},
    {"name": 'Lasso Guard (bottom)', "gi": "true", "image": "/images/positions/Lasso.png"},
    # {"name": 'Spider Guard (top)', "gi": "true", "image": "/images/positions/spider-guard.jpg"},
    {"name": 'Spider Guard (bottom)', "gi": "true", "image": "/images/positions/spider-guard.jpg"},
    # {"name": 'De La Riva Guard (top)', "gi": "true", "image": "/images/positions/De-La-Riva-1.png"},
    {"name": 'De La Riva Guard (bottom)', "gi": "true", "image": "/images/positions/De-La-Riva-1.png"},
    {"name": 'Gyaku-Kesagatame (top)', "image": "/images/positions/gyaku-kesagatame.webp"},
    # {"name": 'Gyaku-Kesagatame (bottom)', "image": "/images/positions/gyaku-kesagatame.webp"},
    {"name": 'Kuzure-Kesagatame (top)', "image": "/images/positions/kuzure-kesagatame.webp"},
    # {"name": 'Kuzure-Kesagatame (bottom)', "image": "/images/positions/kuzure-kesagatame.webp"},
    {"name": 'Kesa Gatame (top)', "image": "/images/positions/Kesa-Getame-1.png"},
    {"name": 'S-Mount (top)', "image": "/images/positions/s-mount.webp"},
    # {"name": 'S-Mount (bottom)', "image": "/images/positions/s-mount.webp"},
    {"name": 'Turtle Backpack (top)', "image": "/images/positions/turtle_backpack.webp"},
    # {"name": 'Turtle Backpack (bottom)', "image": "/images/positions/turtle_backpack.webp"},
    # {"name": 'Seated Guard (top)', "image": "/images/positions/Seated-Guard.png"},
    {"name": 'Seated Guard (bottom)', "image": "/images/positions/Seated-Guard.png"},
    {"name": '50/50 Guard', "gi": "false", "image": "/images/positions/5050-guard.jpg"},
    {"name": 'X-Guard'},
    {"name": 'Deep Half Guard'}, {"name": 'Rubber Guard'},
    {"name": 'Worm Guard', "gi": "true"}, {"name": 'Reverse De La Riva Guard'},
    {"name": 'Berimbolo', "gi": "true", "image": "/images/positions/Berimbolo BJJ.jpeg"},
    {"name": 'Inverted Guard'},
    {"name": 'Single Leg X-Guard'},
    {"name": 'Dog Fight', "image": "/images/positions/dog-fight.webp"},
    {"name": 'Crab Ride'},
    {"name": 'Standing', "image": "/images/positions/stanging-gi.jpg"},
    {"name": 'Knee Shield'},
    {"name": 'Scoop Position'},
    {"name": 'Kesa Gatame', "image": "/images/positions/Kesa-Getame-1.png"},
    {"name": 'Reverse Kesa Gatame'},
    {"name": 'Shin on Shin'},
    {"name": 'High Mount'},
    {"name": 'Crucifix'},
    {"name": 'Body Lock', "image": "/images/positions/body_lock.webp"},

]

positions_to_position = [
    # Side Control (top) to kesagatame
    {"position1": 'Side Control (top)', "position2": 'Kesa Gatame'},
    {"position1": 'Side Control (top)', "position2": 'Reverse Kesa Gatame'},
    {"position1": 'Side Control (top)', "position2": 'North-South (top)'},
    {"position1": 'Closed Guard (bottom)', "position2": 'Open Guard (bottom)'},
    {"position1": 'Open Guard (bottom)', "position2": 'Closed Guard (bottom)'},
    {"position1": 'Half Guard', "position2": 'Side Control (bottom)'},
    {"position1": 'Half Guard', "position2": 'Deep Half Guard'},
    {"position1": 'Side Control (top)', "position2": 'Knee on Belly (top)'},
    {"position1": 'Knee on Belly (top)', "position2": 'Seated Mount (top)'},
    # Seated Mount (top) to high mount
    {"position1": 'Seated Mount (top)', "position2": 'High Mount'},
    # high mount to Back Control (take)
    {"position1": 'High Mount', "position2": 'Back Control (take)'},
    #high mount to s-mount
    {"position1": 'High Mount', "position2": 'S-Mount (top)'},
    # Open Guard (bottom) to shin on shin
    {"position1": 'Open Guard (bottom)', "position2": 'Shin on Shin'},
    {"position1": 'Turtle (top)', "position2": 'Truck (take)'},
    #turtle top to turtle back pack top
    {"position1": 'Turtle (top)', "position2": 'Turtle Backpack (top)'},
    #open guard bottom to butterfly guard bottom
    {"position1": 'Open Guard (bottom)', "position2": 'Butterfly Guard (bottom)'},
    #open guard bottom to lasso guard bottom
    {"position1": 'Open Guard (bottom)', "position2": 'Lasso Guard (bottom)'},
    #open guard bottom to spider guard bottom
    {"position1": 'Open Guard (bottom)', "position2": 'Spider Guard (bottom)'},
    #open guard bottom to de la riva guard bottom
    {"position1": 'Open Guard (bottom)', "position2": 'De La Riva Guard (bottom)'},

]

position_to_submission = [
    {"position": "Back Control (take)", "submission": "Bow and Arrow Choke"},
    {"position": "Back Control (take)", "submission": "Rear Naked Choke"},
    {"position": "Back Control (take)", "submission": "Reversed Triangle-Choke"},
    {"position": "Open Guard (bottom)", "submission": "Armbar"},
    {"position": "Closed Guard (bottom)", "submission": "Ezekiel Choke"},
    {"position": "Closed Guard (bottom)", "submission": "Guillotine Choke"},
    {"position": "Closed Guard (bottom)", "submission": "Kimura"},
    {"position": "Closed Guard (bottom)", "submission": "Loop Choke"},
    {"position": "Open Guard (bottom)", "submission": "Omoplata"},
    {"position": "Open Guard (bottom)", "submission": "Triangle-Choke"},
    {"position": "Closed Guard (bottom)", "submission": "Wrist Lock"},
    {"position": "High Mount", "submission": "Mounted Triangle"},
    {"position": "Seated Mount (top)", "submission": "Arm Triangle"},
    {"position": "High Mount", "submission": "Armbar"},
    {"position": "Side Control (top)", "submission": "Americana"},
    {"position": "Side Control (top)", "submission": "Arm Triangle"},
    {"position": "Side Control (top)", "submission": "Kimura"},
    {"submission": "D'Arce Choke", "position": 'Side Control (top)'},
    {"position": "Truck (take)", "submission": "Banana Split"},
    {"position": "Truck (take)", "submission": "Twister"},
    #Figure Four Submission from mount
    {"position": "Seated Mount (top)", "submission": "Figure Four Submission"},
    {"submission": "D'Arce Choke", "position": 'Turtle (top)'},
    {"submission": 'Anaconda Choke', "position": 'Turtle (top)'},
    #Half Guard (top) to Kimura
    {"position": "Half Guard (top)", "submission": "Kimura"},
    #and darce choke
    {"position": "Half Guard (top)", "submission": "D'Arce Choke"},
    #side control (bottom) to buggy choke
    {"position": "Side Control (bottom)", "submission": "Buggy Choke"},
    #north south choke from north south top
    {"position": "North-South (top)", "submission": "North South Choke"},

]

positions_using_transition = [
    {"transition": 'Scissor Sweep', "position": 'Open Guard (bottom)'},
    {"transition": 'Flower Sweep', "position": 'Open Guard (bottom)'},
    {"transition": 'Hip Bump Sweep', "position": 'Open Guard (bottom)'},
    {"transition": 'Deep Half Guard', "position": 'Half Guard (bottom)'},
    # double leg takedown from standing to Side Control (top)
    {"transition": 'Double Leg Takedown', "position": 'Standing'},
    # single leg takedown from standing to half guard
    {"transition": 'Single Leg Takedown', "position": 'Standing'},
    # butterfly sweep from Butterfly Guard (bottom)
    {"transition": 'Butterfly Sweep', "position": 'Butterfly Guard (bottom)'},
    # single leg from shin on shin
    {"transition": 'Single Leg Takedown', "position": 'Shin on Shin'},

]

positions_escaping_with_escape = [
    {"escape": 'Granby Roll', "position": 'Omoplata'},
    {"escape": 'Elbow Escape', "position": 'Side Control (bottom)'},
    {"escape": 'Hip Escape', "position": 'Side Control (bottom)'},
    {"escape": 'Turtle Escape', "position": 'Turtle (bottom)'},
    {"escape": 'Scooping', "position": 'Back Control (taken)'},
    {"escape": 'Can Opener', "position": 'Closed Guard (top)'},
    {"escape": 'Knee Slide Pass', "position": 'Open Guard (top)'},
    #side control with Kimura Sweep
    {"escape": 'Kimura Sweep', "position": 'Side Control (buttom)'},

]