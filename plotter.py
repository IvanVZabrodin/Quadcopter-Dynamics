import simulation as sim
import matplotlib.pyplot as plt
import numpy as np
from emath import *

simulation_time = 100
sampletime = 0.1
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

print("Final Position:", drone.position.z)


fig = plt.figure(constrained_layout=True)

posax = plt.subplot2grid((3, 3), (0, 0), projection='3d', fig=fig)

posax.scatter(x[0], y[0], z[0], c='g', s=dotsize)
posax.scatter(x[-1], y[-1], z[-1], c='r', s=dotsize)

posp = posax.plot(x, y, z, color='black')
posax.set_title('Position')

rotax = plt.subplot2grid((3, 3), (0, 2), projection='3d', fig=fig)

rotax.scatter(rx[0], ry[0], rz[0], c='g', s=dotsize)
rotax.scatter(rx[-1], ry[-1], rz[-1], c='r', s=dotsize)

rotp = rotax.plot(rx, ry, rz, color='black')
rotax.set_title('Rotation')


timexax = np.arange(0.0, simulation_time, sampletime)


txax = plt.subplot2grid((3, 3), (1, 0), fig=fig)

txp = txax.plot(timexax, x, color='black')
txax.set_title('X position over time')
txax.set_xlabel('Time (s)')
txax.set_ylabel('Position (m)')


tyax = plt.subplot2grid((3, 3), (1, 1), fig=fig)

typ = tyax.plot(timexax, y, color='black')
tyax.set_title('Y position over time')
tyax.set_xlabel('Time (s)')
tyax.set_ylabel('Position (m)')


tzax = plt.subplot2grid((3, 3), (1, 2), fig=fig)

tzp = tzax.plot(timexax, z, color='black')
tzax.set_title('Z position over time')
tzax.set_xlabel('Time (s)')
tzax.set_ylabel('Position (m)')


trxax = plt.subplot2grid((3, 3), (2, 0), fig=fig)

txp = trxax.plot(timexax, rx, color='black')
trxax.set_title('X rotation over time')
trxax.set_xlabel('Time (s)')
trxax.set_ylabel('Rotation (rad)')


tryax = plt.subplot2grid((3, 3), (2, 1), fig=fig)

typ = tryax.plot(timexax, ry, color='black')
tryax.set_title('Y rotation over time')
tryax.set_xlabel('Time (s)')
tryax.set_ylabel('Rotation (rad)')


trzax = plt.subplot2grid((3, 3), (2, 2), fig=fig)

tzp = trzax.plot(timexax, rz, color='black')
trzax.set_title('Z rotation over time')
trzax.set_xlabel('Time (s)')
trzax.set_ylabel('Rotation (rad)')


plt.show()
