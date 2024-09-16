# Build a program that asks the user to enter the length and width of a room, 
# in meters, then prints the room's area in both square meters and square feet.

# Modify the program to let the user specify the measurement type (meters or feet). 
# Compute the area accordingly and print it and its conversion in parentheses.

SQ_METER_IN_FT = 10.7639 # 1 sq meter = 10.7639 sq ft

def room_size():
    
    units = input('Do you want to use feet or meters? (type feet or meters): ').lower()
    
    while not (units.startswith('f') or units.startswith('m')):
        units = input('Invalid selection, please type feet or meters: ')
    
    width = float(input(f'What is the width in {units}? ')) 
    length = float(input(f'What is the length in {units}? ')) 
    
    if units.startswith('m'):
        area_in_meters = width * length
        area_in_feet = area_in_meters * SQ_METER_IN_FT
        
        print(f'The size of the room is {area_in_meters:.2f} sq meters.')
        print(f'The size of the room is {area_in_feet:.2f} sq feet.')

    elif units.startswith('f'):
        area_in_feet = width * length
        area_in_meters = area_in_feet / SQ_METER_IN_FT
        
        print(f'The size of the room is {area_in_feet:.2f} sq feet.')
        print(f'The size of the room is {area_in_meters:.2f} sq meters.')

room_size()