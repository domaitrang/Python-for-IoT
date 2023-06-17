import math


def cv_hinh_tron(r: float) -> float:
    if (r <= 0):
        return -1
    cv = 2*math.pi*r
    return cv


def dt_hinh_tron(r: float) -> float:
    if (r <= 0):
        return -1
    dt = math.pi * r*r
    return dt
