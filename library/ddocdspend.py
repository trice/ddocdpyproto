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
    and calculate an ability range to use. The trick is to just figure
    out how far this method should index into the build_points array
    '''
    build_points = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3]

    ability_range = []
    if points_available == 0:
        return [8]

    # 16 is the most points you can spend on an ability
    max_points = 16

    points_max = points_available
    if points_available >= max_points:
        points_max = max_points

    points_spent = 0
    index = 0

    while points_spent <= points_max:
        ability_range.append(8 + index)
        if index == 10:
            break
        points_spent += build_points[index]
        index += 1

    return ability_range
