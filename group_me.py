from typing import Callable, List, Dict

def group(f: Callable, vals: List) -> Dict:
    '''
    :f: function that runs on elements of 'vals'
    :vals: list of arguments to pass to function
    :return: dictionary of values: results
    '''
    ret = {}

    for val in vals:
        ret[val] = f(val)
    return ret

def mod_three(num: int) -> int:
    return num % 3

if __name__ == "__main__":
    print(group(mod_three, [0, 1, 2, 4, 5, 6]))