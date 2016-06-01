import datetime


def move():
    '''
    simulate the movement from Y to X
    '''


    turning_points = []
    #routes = []
    routes = 0
    size_x = 20
    size_y = 20

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
                    if previous_position[1] != last_position[1] and last_position[0] != size_y:
                        last_turning_point = last_position
                        #print last_turning_point

                move_x += 1
                if move_x > size_x or (move_y, move_x) in turning_points:
                    break

            move_y += 1
            if move_y > size_y:
                break

        ' if prev route turning point x index is different than current last turning point then set the turning points to last turning point only + previous y,1 indexes'
        if len(turning_points) > 1 and turning_points[-1][1] != last_turning_point[1]:
            temp_points = []
            for point in turning_points:
                if point[0] < last_turning_point[0] or point[1] < last_turning_point[1]:
                    temp_points.append(point)
            turning_points = temp_points

        turning_points.append(last_turning_point)

        #print route
        #print len(turning_points)

        #routes.append(route)
        routes += 1

        # ' if the route contains the bottom left (size y, 0), means that's the last route
        if (size_y, 0) in route:
            break

    #print len(routes)
    print routes


start_time = datetime.datetime.now()

move()

end_time = datetime.datetime.now()

duration = end_time - start_time
print duration