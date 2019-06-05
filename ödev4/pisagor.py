def pisagor():
    i = 0
    for x in range (1,101):
        for y in range (1,101):
            for z in range (1,101):
                if (x*x + y*y == z*z and x<y and y<z and x<z):
                    i+= 1
                    print ("{}.Pisagor:{},{},{}".format (i,x,y,z))
pisagor()

