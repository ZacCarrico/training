from random import randint

def egg_drop_simulation(floors):
    too_high_floor = randint(1, floors) # egg will break if dropped from this floor
    step_tries = {}
    for step_size in range(1, floors + 1):
        egg1 = egg2 = True
        current_floor = 0
        tries = 0
        while egg1:
            tries += 1
            previous_floor = current_floor
            current_floor = current_floor + step_size
            if current_floor >= floors:
                current_floor = floors
            if current_floor >= too_high_floor:
                egg1 = False
        current_floor = previous_floor
        while egg2:
            tries += 1
            current_floor += 1
            if current_floor == too_high_floor:
                highest_safedrop = max(current_floor - 1, 0)
                egg2 = False
        step_tries[step_size] = tries
        assert(highest_safedrop == too_high_floor - 1)
    return step_tries

def agg_results(floors, n):
    aggd = [0] * floors
    for _ in range(n):
        result = egg_drop_simulation(floors)
        for i, value in enumerate(result.values()):
            aggd[i] += value
    avgs = [_/n for _ in aggd]
    return avgs

def get_min_index(floors, n):
    avgs = agg_results(floors, n)
    min_val = floors + 1
    for i, val in enumerate(avgs):
        if val <= min_val:
            min_val = val
            min_index = i
    return min_index, min_val

print(get_min_index(100, 10000))