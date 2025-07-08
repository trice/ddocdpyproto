def point_spender(start, end, points_available):
    '''
    point_spender will take the chosen ability score value
    and then deduce the cost of it from the points_available
    and then return the new balance of points available for use.
    '''
    build_points = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3]

    points_spent = 0
    for i in range((end-start)):
        points_spent -= build_points[i]

    return points_available - points_spent


def get_ability_range(points_available):
    '''
    get_ability_range will take the amount of points that are available
    and calculate an ability range to use for the range of options possible
    for all ability scores
    '''
    build_points = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3]

    if points_available == 0:
        return [8]

    ability_range = []
    points_spent = 0
    for i in range(points_available):
        for i in range(12):
            points_spent += build_points[i]
            if 12 > points_spent:
                ability_range.append(8+i)
            else:
                break
    return ability_range
