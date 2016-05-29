

def move():
    '''
    simulate the movement from Y to X
    '''

    
    turning_points = []
    routes = []
    size_x = 3
    size_y = 3

    while True:

        route = []
        last_position = (0, 0)

        move_y = 0
        while True:
            move_x = 0
            while True:
                if move_y >= last_position[0] and move_x >= last_position[1]:
                    previous_position = last_position
                    last_position = (move_y, move_x)
                    route.append(last_position)
                    #print last_position
                    if previous_position[1] != last_position[1] and last_position != (size_y, size_x):
                        last_turning_point = last_position
                        #print 'Turning Point:' + str(last_turning_point)

                move_x += 1
                if move_x > size_x or (move_y, move_x) in turning_points:
                    break

            move_y += 1
            if move_y > size_y:
                break

        print route

        # ' clear the turning points for new Y route calculation
        if last_turning_point == (0, 1):
            turning_points = []
        turning_points.append(last_turning_point)
        routes.append(route)

        # ' if the last turning point is the same as the height, means this is the last route
        if last_turning_point[0] == size_y:
            break

    print len(routes)


move()
