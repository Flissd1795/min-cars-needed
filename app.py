from validation import validate_inputs

def min_cars_needed(P, S):
    validate_inputs(P, S)  # Validate inputs before proceeding
    total_people = sum(P)  # Calculates total number of people
    if total_people == 0:  # If no people, return 0
        return 0

    sorted_seats = sorted(S, reverse=True) # Sort seats in descending order so we can use cars with the most seats first

    seats_secured = 0    # Counts the total number of seats needed
    cars_used = 0        # Counts the number of cars used

    for seats in sorted_seats:               # Iterates through the sorted list of seats
        seats_secured += seats               # Adds all the seats from this car to the total seat count
        cars_used += 1                       # Once all seats added from that car, add to the car count
        if seats_secured >= total_people:
            return cars_used                 # If we have enough seats, return the number of cars used

    raise ValueError("There are not enough cars to seat the entire group")  # If we exit the loop without having enough seats, raise an error   


print(min_cars_needed([1, 4, 1], [1, 5, 1]))            # Returns 2
print(min_cars_needed([4, 4, 2, 4], [5, 5, 2, 5]))      # Returns 3
print(min_cars_needed([2, 3, 4, 2], [2, 5, 7, 2]))      # Returns 2