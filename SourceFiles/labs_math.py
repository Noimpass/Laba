from typing import Union
import numpy as np


UIF = Union[int, float]
NUIF = Union[None, UIF]

class FirstMathClass:
    def calc_line_resistance_complex(
        self,
        af: UIF,
        x: UIF = 10,
        cv: complex = 10j,
    ) -> UIF:
        return x + cv * af

    def calc_line_impedance_capacitive(
        self,
        af: UIF,
        x: UIF = 0.42,
        cv: complex = -1j
    ) -> UIF:
        return np.round(cv/(af * x), 2)

    def calc_load_reactance_inductive(
        self,
        af: UIF,
        x: UIF = 0,
        cv: complex = 50j
    ) -> UIF:
        return x + cv * af

    def calc_load_reactance_capacitive(
        self,
        af: UIF,
        x: UIF = 0,
        cv: complex = 50j
    ) -> UIF:
        return x - cv * af

    def calc_resistance_comlpex_uncompensated(
        self,
        lri: UIF,
        lra: UIF,
    ) -> UIF:
        return lri + lra

    def calc_load_resistance_complex_compensated(
        self,
        lrc: UIF,
        lrcu: UIF,
    ) -> UIF:
        return (lrc * lrcu)/(lrc+lrcu)

    def calc_circuit_resistance_complex(
        self,
        lrscc: UIF,
        lrc: UIF,
    ) -> UIF:
        return lrscc + lrc

    def calc_circuit_current_complex(
        self,
        iv: UIF,
        crc: UIF,
    ) -> UIF:
        return iv / crc

    def calc_circuit_power(
        self,
        cmd: str = "complex",
        ccc: NUIF = None,
        crc: NUIF = None,
        ccp: NUIF = None,
    ) -> UIF:
        if cmd == 'complex' and ccc is not None or crc is not None:
            return ccc * (crc ** 2)
        elif cmd == 'active' and ccp is not None:
            return np.real(ccp)
        elif cmd == 'reactive' and ccp is not None:
            return np.imag(ccp)
        elif cmd == 'apparent' and ccp is not None:
            return np.abs(ccp)
    
    def calc_line_power(
        self,
        cmd: str = 'complex',
        ccc: NUIF = None,
        lrc: NUIF = None,
        lcp: NUIF = None,
    ) -> UIF:
        return self.calc_circuit_power(cmd=cmd, ccc=ccc, crc=lrc, ccp=lcp)

    def calc_uncompensated_power(
        self,
        cmd: str = 'complex',
        ccc: NUIF = None,
        lrcu: NUIF = None,
        lucp: NUIF = None,
    ) -> UIF:
        return self.calc_circuit_power(cmd=cmd, ccc=ccc, crc=lrcu, ccp=lucp)

    def calc_compensated_power(
        self,
        cmd: str = 'complex',
        ccc: NUIF = None,
        lrcc: NUIF = None,
        lccp: NUIF = None,
    ) -> UIF:
        return self.calc_circuit_power(cmd=cmd, ccc=ccc, crc=lrcc, ccp=lccp)

    
