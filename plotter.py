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

import pidsimulation as sim
import matplotlib.pyplot as plt
from emath import *

simulation_time = 100
sampletime = 0.1
rendertime = 0.1 # Make smaller for more accuracy, larger for performance - but not much, because mpl is very slow
dotsize = 1
destination = Vector4(0, 0, 100, 0)

drone = sim.Drone(destination)

x, y, z = [0.0], [0.0], [0.0]
rx, ry, rz = [0.0], [0.0], [0.0]


for _ in range(int(simulation_time // sampletime)):
    drone.update(sampletime)

    x.append(drone.position.x)
    y.append(drone.position.y)
    z.append(drone.position.z)
    
    rx.append(drone.rotation.x)
    ry.append(drone.rotation.y)
    rz.append(drone.rotation.z)

print("Final Position:", drone.position, "Final Rotation:", drone.rotation, "Points simulated:", int(simulation_time // sampletime) + 1)


def create_plot_row(dim: tuple[int, int], ypos: int, xlabel: str, ylabel: str, fig: plt.Figure) -> list[plt.Axes]:
    res = []
    for x in range(dim[1]):
        res.append(plt.subplot2grid(dim, (ypos, x), fig=fig, xlabel=xlabel, ylabel=ylabel))
    return res


def create_vector_plot(dim: tuple[int, int], pos: tuple[int, int], xv: list[float], yv: list[float], zv: list[float], start_color, end_color) -> plt.Axes:
    newx = plt.subplot2grid(dim, pos, projection='3d', fig=fig)

    newx.scatter(xv[0], yv[0], zv[0], c=start_color, s=2)
    newx.scatter(xv[-1], yv[-1], zv[-1], c=end_color, s=2)

    newx.plot(x, y, z, color='black')

    return newx


def sample_for_render(sampletime: float, rendertime: float, points: list[float]) -> list[float]:
    selectionstep = int(rendertime // sampletime)
    res = points[::selectionstep]
    return res


fig = plt.figure(constrained_layout=True)

[sx, sy, sz] = list(map(lambda p: sample_for_render(sampletime, rendertime, p), [x, y, z]))
[srx, sry, srz] = list(map(lambda p: sample_for_render(sampletime, rendertime, p), [rx, ry, rz]))

# 3D Graphs
posvecplot = create_vector_plot((3, 3), (0, 0), sx, sy, sz, 'g', 'r')
posvecplot.set_title('Position')

rotvecplot = create_vector_plot((3, 3), (0, 2), srx, sry, srz, 'g', 'r')
rotvecplot.set_title('Rotation')



# 2D Graphs
timeax = frange(0.0, simulation_time, sampletime)

# Position
posplots = create_plot_row((3, 3), 1, "Time (s)", "Position (m)", fig)

posplots[0].plot(timeax, x, color='black')
posplots[0].set_title('X position over time')

posplots[1].plot(timeax, y, color='black')
posplots[1].set_title('Y position over time')

posplots[2].plot(timeax, z, color='black')
posplots[2].set_title('Z position over time')

# Rotation
rotplots = create_plot_row((3, 3), 2, "Time (s)", "Rotation (rad)", fig)

rotplots[0].plot(timeax, rx, color='black')
rotplots[0].set_title('X rotation over time')

rotplots[1].plot(timeax, ry, color='black')
rotplots[1].set_title('Y rotation over time')

rotplots[2].plot(timeax, rz, color='black')
rotplots[2].set_title('Z rotation over time')


plt.show()
