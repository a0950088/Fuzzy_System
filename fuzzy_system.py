FRONT_CLOSE = 15
FRONT_MODERATE = [10, 25]
FRONT_FAR = 20
BIG_LEAN_LEFT = -15
MIDDLE_LEAN_LEFT = [-17, -10]
SMALL_LEAN_LEFT = [-12, 0]
BIG_LEAN_RIGHT = 15
MIDDLE_LEAN_RIGHT = [10, 17]
SMALL_LEAN_RIGHT = [0, 12]

def fuzzySystem(front, left_minus_right):
    theta_list = []
    if left_minus_right <= 0:
        #turn right
        if front < FRONT_CLOSE and left_minus_right < BIG_LEAN_LEFT:
            theta_list.append(40)
        if FRONT_MODERATE[0]<front and front<FRONT_MODERATE[1] and left_minus_right < BIG_LEAN_LEFT:
            theta_list.append(30)
        if front > FRONT_FAR and left_minus_right < BIG_LEAN_LEFT:
            theta_list.append(25)
        if front < FRONT_CLOSE and MIDDLE_LEAN_LEFT[0]<left_minus_right and left_minus_right<MIDDLE_LEAN_LEFT[1]:
            theta_list.append(35)
        if FRONT_MODERATE[0]<front and front<FRONT_MODERATE[1] and MIDDLE_LEAN_LEFT[0]<left_minus_right and left_minus_right<MIDDLE_LEAN_LEFT[1]:
            theta_list.append(25)
        if front > FRONT_FAR and MIDDLE_LEAN_LEFT[0]<left_minus_right and left_minus_right<MIDDLE_LEAN_LEFT[1]:
            theta_list.append(10)
        if front < FRONT_CLOSE and SMALL_LEAN_LEFT[0]<left_minus_right and left_minus_right<=SMALL_LEAN_LEFT[1]:
            theta_list.append(25)
        if FRONT_MODERATE[0]<front and front<FRONT_MODERATE[1] and SMALL_LEAN_LEFT[0]<left_minus_right and left_minus_right<=SMALL_LEAN_LEFT[1]:
            theta_list.append(15)
        if front > FRONT_FAR and SMALL_LEAN_LEFT[0]<left_minus_right and left_minus_right<=SMALL_LEAN_LEFT[1]:
            theta_list.append(5)
    else:
        #turn left
        if front < FRONT_CLOSE and left_minus_right > BIG_LEAN_RIGHT:
            theta_list.append(-40)
        if FRONT_MODERATE[0]<front and front<FRONT_MODERATE[1] and left_minus_right > BIG_LEAN_RIGHT:
            theta_list.append(-30)
        if front > FRONT_FAR and left_minus_right > BIG_LEAN_RIGHT:
            theta_list.append(-25)
        if front < FRONT_CLOSE and MIDDLE_LEAN_RIGHT[0]<left_minus_right and left_minus_right<MIDDLE_LEAN_RIGHT[1]:
            theta_list.append(-35)
        if FRONT_MODERATE[0]<front and front<FRONT_MODERATE[1] and MIDDLE_LEAN_RIGHT[0]<left_minus_right and left_minus_right<MIDDLE_LEAN_RIGHT[1]:
            theta_list.append(-25)
        if front > FRONT_FAR and MIDDLE_LEAN_RIGHT[0]<left_minus_right and left_minus_right<MIDDLE_LEAN_RIGHT[1]:
            theta_list.append(-10)
        if front < FRONT_CLOSE and SMALL_LEAN_RIGHT[0]<left_minus_right and left_minus_right<SMALL_LEAN_RIGHT[1]:
            theta_list.append(-25)
        if FRONT_MODERATE[0]<front and front<FRONT_MODERATE[1] and SMALL_LEAN_RIGHT[0]<left_minus_right and left_minus_right<SMALL_LEAN_RIGHT[1]:
            theta_list.append(-15)
        if front > FRONT_FAR and SMALL_LEAN_RIGHT[0]<left_minus_right and left_minus_right<SMALL_LEAN_RIGHT[1]:
            theta_list.append(5)

    return sum(theta_list)/len(theta_list)