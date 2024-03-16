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

    def __mul__(self, val: float | int) -> "Vector4":
        return Vector4(
                self.x * val,
                self.y * val,
                self.z * val,
                self.w * val,
                )

    def __iter__(self):
        return iter([self.x, self.y, self.z, self.w])
