def get_min_gas_stops(some_list, miles_per_tank):
    """Get the min number of gas stops to get from start to finish,
    where miles_per_tank is the max number of miles one can drive before needing
    to stop for gas

    >>> get_min_gas_stops([0, 200, 375, 500, 750, 900], 400)
    2
    """

    start = 0

    stops = []
    i = 0
    j = 1

    while j < (len(some_list)):
        if some_list[j] - start > miles_per_tank:
            # add some_list[i] to list of stops, and set start to some_list[i]
            stops.append(some_list[i])
            start = some_list[i]
        i += 1
        j += 1
    return len(stops)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** All tests passed!\n"
