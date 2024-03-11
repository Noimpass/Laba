# Filename: : lmath.py
# Description: Модуль состоящий из функций, что способны упростить вычисления, их оберток и моделей данных.

from typing import Union
import numpy as np
from .exceptions import CommandNotFoundException

# UNION INT FLOAT
UIF = Union[Union[int, float], complex]
# NONE UNION INT FLOAT
NUIF = Union[None, UIF]
# NONE UNION INT FLOAT OBJECT
NUIFWE = Union[NUIF, object]

# Модель для упрощения вычислений и передачи аргументов.
class AXC:
    def __init__(self: object, angular_frequency: UIF = None, x: UIF = 0, complex_value: NUIF = 10j) -> object:
        self.af = angular_frequency
        self.x = x
        self.cv = complex_value

# Функция-обертка над обьектом AXC и коммандой для упрощения вычисления.
def axc_wrapper(obj: AXC, cmd: str = '+') -> NUIFWE:
    if cmd == '+':
        return obj.x + obj.cv * obj.af
    elif cmd == '-':
        return obj.x - obj.cv * obj.af
    else:
        return CommandNotFoundException()

def numpy_wrapper(obj: AXC = None, cmd: str = '') -> NUIF:
    return object

def calc_circuit_power(
    cmd: str = "complex",
    ccc: NUIF = None,
    crc: NUIF = None,
    ccp: NUIF = None,
) -> NUIFWE:
    if cmd == 'complex' and ccc is not None or crc is not None:
        return ccc * (crc ** 2)
    elif cmd == 'active' and ccp is not None:
        return np.real(ccp)
    elif cmd == 'reactive' and ccp is not None:
        return np.imag(ccp)
    elif cmd == 'apparent' and ccp is not None:
        return np.abs(ccp)
    else:
        return CommandNotFoundException()


def calc_impedance_capacitive(obj: AXC = None) -> NUIFWE:
    return np.round(obj.cv/(obj.af * obj.x), 2)

def calc_resistance_complex_uncompensated(lri: UIF, lra: UIF) -> NUIF:
    return lri + lra

def calc_load_resistance_complex_compensated(lrc: UIF, lrcu: UIF) -> UIF:
    return (lrc * lrcu)/(lrc+lrcu)


def calc_load_resistance_complex_compensated(
    self,
    lrc: UIF,
    lrcu: UIF,
) -> UIF:
    return (lrc * lrcu)/(lrc+lrcu)

def calc_circuit_resistance_complex(
    lrscc: UIF,
    lrc: UIF,
) -> UIF:
    return lrscc + lrc

def calc_circuit_current_complex(
    iv: UIF,
    crc: UIF,
) -> UIF:
    return iv / crc
    
def calc_line_power(
    cmd: str = 'complex',
    ccc: NUIF = None,
    lrc: NUIF = None,
    lcp: NUIF = None,
) -> UIF:
    return calc_circuit_power(cmd=cmd, ccc=ccc, crc=lrc, ccp=lcp)

def calc_uncompensated_power(
    cmd: str = 'complex',
    ccc: NUIF = None,
    lrcu: NUIF = None,
    lucp: NUIF = None,
) -> UIF:
    return calc_circuit_power(cmd=cmd, ccc=ccc, crc=lrcu, ccp=lucp)

def calc_compensated_power(
    cmd: str = 'complex',
    ccc: NUIF = None,
    lrcc: NUIF = None,
    lccp: NUIF = None,
) -> UIF:
    return calc_circuit_power(cmd=cmd, ccc=ccc, crc=lrcc, ccp=lccp)


