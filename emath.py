"""
    Quadcopter simulation
    Copyright (C) 2024  Ivan Zabrodin

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

#  For things like Vector3 implementations for readable code

class Vector3:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, key: int) -> float:
        return [self.x, self.y, self.z][key]

    def __setitem__(self, key: int, value: float | int) -> None:
        [self.x, self.y, self.z][key] = value

    def __add__(self, vec: "Vector3 | tuple[float, float, float]") -> "Vector3":
        return Vector3(
                self.x + vec[0],
                self.y + vec[1],
                self.z + vec[2],
                )

    def __sub__(self, vec: "Vector3 | tuple[float, float, float]") -> "Vector3":
        return Vector3(
                self.x - vec[0],
                self.y - vec[1],
                self.z - vec[2],
                )

    def __mul__(self, val: float | int) -> "Vector3":
        return Vector3(
                self.x * val,
                self.y * val,
                self.z * val,
                )

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

class Vector4:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 0.0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __getitem__(self, key: int) -> float:
        return [self.x, self.y, self.z, self.w][key]

    def __setitem__(self, key: int, value: float | int) -> None:
        [self.x, self.y, self.z, self.w][key] = value

    def __add__(self, vec: "Vector4 | tuple[float, float, float, float]") -> "Vector4":
        return Vector4(
                self.x + vec[0],
                self.y + vec[1],
                self.z + vec[2],
                self.w + vec[3],
                )

    def __sub__(self, vec: "Vector4 | tuple[float, float, float, float]") -> "Vector4":
        return Vector4(
                self.x - vec[0],
                self.y - vec[1],
                self.z - vec[2],
                self.w - vec[3],
                )

    def __mul__(self, val: "float | int | Vector4") -> "Vector4":
        if isinstance(val, Vector4):
            return Vector4(
                    self.x * val.x,
                    self.y * val.y,
                    self.z * val.z,
                    self.w * val.w,
                    )
        return Vector4(
                self.x * val,
                self.y * val,
                self.z * val,
                self.w * val,
                )

    def __iter__(self):
        return iter([self.x, self.y, self.z, self.w])

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

def frange(start: float, end: float, step: float) -> list[float]:
    res = []
    for n in range(int(start // step), int((end - start) // step) + 1):
        res.append(n * step)
    return res
