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


from math import pi
from emath import *

class WorldData:
    inertia = Vector3(0.015, 0.015, 0.01)
    gravity = 9.8
    mass = 0.8

class Drone:
    def __init__(self, destination: Vector4) -> None:
        self.dest = destination

        self.position = Vector3()
        self.rotation = Vector3()
        
        self.positional_vel = Vector3()
        self.rotational_vel = Vector3()

        self.inputs = Vector4()

        self.error = destination
        self.previous_error = destination
        self.error_total = destination

        #  Constants
        self.kf, self.kt = 1, 1
        self.kp = Vector4(0.4, 0.4, 1.6, 0)
        self.ki = Vector4(0.01, 0.01, 0.005, 0)
        self.kd = Vector4(3, 3, 32, 0)
        self.rotor_length = 0.25
        self.error_margin = 0.01

    def update(self, dt: float) -> bool:
        self.update_simulation(dt)
        self.update_error()

        if (self.within_margin()):
            self.inputs = Vector4(0, 0, WorldData.gravity, 0)
            return True

        self.update_inputs() 
        
        return False

    def within_margin(self) -> bool:
        return max(max(self.error), abs(min(self.error))) <= self.error_margin # type: ignore
                
    def update_error(self) -> None:
        self.previous_error = self.error
        self.error = self.dest - (
                (self.rotation.x % (2 * pi)),
                (self.rotation.y % (2 * pi)),
                self.position.z,
                (self.rotation.z % (2 * pi)),
                )
        self.error_total += self.error
    
    def update_inputs(self) -> None:
        self.inputs = ((self.error * self.kp)
                    + (self.error_total * self.ki)
                    + (self.error - self.previous_error)
                    * self.kd)
    
    def get_position_acc(self) -> Vector3:
        x = (self.rotation.x * WorldData.gravity)

        y = (self.rotation.y * WorldData.gravity)

        z = (self.inputs.z / WorldData.mass) - WorldData.gravity
        
        return Vector3(x, y, z)

    def get_rotation_acc(self) -> Vector3:
        x = ((self.rotor_length * self.inputs.x
          - (WorldData.inertia.z - WorldData.inertia.y)
          * (self.rotational_vel.y * self.rotational_vel.z))
          / WorldData.inertia.x)

        y = ((self.rotor_length * self.inputs.y
          - (WorldData.inertia.x - WorldData.inertia.z)
          * (self.rotational_vel.x * self.rotational_vel.z))
          / WorldData.inertia.y)

        z = (((self.kt / self.kf) * self.inputs.w
          - (WorldData.inertia.y - WorldData.inertia.x)
          * (self.rotational_vel.x * self.rotational_vel.y))
          / WorldData.inertia.z)
        
        return Vector3(x, y, z)


    def update_simulation(self, dt: float) -> None:
        position_acc = self.get_position_acc()
        rotation_acc = self.get_rotation_acc()

        self.positional_vel += position_acc * dt
        self.rotational_vel += rotation_acc * dt
        
        self.position += self.positional_vel * dt
        self.rotation += self.rotational_vel * dt
