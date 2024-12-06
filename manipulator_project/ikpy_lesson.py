# import ikpy.chain
# import numpy as np
# import ikpy.utils.plot as plot_utils
#
# my_chain = ikpy.chain.Chain.from_urdf_file("poppy_ergo.URDF")
#
# target_position = [0.5, -0.2, 0.5]
# print("The angles of each joints are: ", my_chain.inverse_kinematics(target_position))
#
# real_frame = my_chain.forward_kinematics(my_chain.inverse_kinematics(target_position))
# print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_position))
#
# import matplotlib.pyplot as plt
# fig, ax = plot_utils.init_3d_figure()
# my_chain.plot(my_chain.inverse_kinematics(target_position), ax, target=target_position)
# plt.xlim(-0.1, 0.1)
# plt.ylim(-0.1, 0.1)
# plt.show()

from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
import numpy as np
import matplotlib.pyplot as plt
import ikpy.utils.plot as plot_utils

# Определение звеньев
link1 = URDFLink(
    name="link1",
    bounds=(-np.pi, np.pi),
    origin_translation=np.array([0.0, -0.5, 3]),
    origin_orientation=np.array([0.0, 0.0, 0.0]),
    rotation=np.array([0.0, 1.0, 0.0]),
    joint_type="revolute"
)

# link2 = URDFLink(
#     name="link2",
#     bounds=(-np.pi, np.pi),
#     origin_translation=np.array([0.0, 0.0, 2]),
#     origin_orientation=np.array([0.0, 0.0, 0.0]),
#     rotation=np.array([0.0, 1.0, 0.0]),
#     joint_type="revolute"
# )
#
# link3 = URDFLink(
#     name="link3",
#     bounds=(-np.pi, np.pi),
#     origin_translation=np.array([0.0, 0.0, 0.5]),
#     origin_orientation=np.array([0.0, 0.0, 0.0]),
#     rotation=np.array([0.0, 0.0, 1.0]),
#     joint_type="revolute"
# )

# Создание кинематической цепи
my_chain = Chain(links=[
    OriginLink(),
    link1
    # link2
    # link3
])

# Решение обратной задачи кинематики
target_position = [0.5, 0.5, 0.5]
target_orientation = [1, 0.5, 0.5, 0.5]  # Вектор ориентации (кватернион)

joint_angles = my_chain.inverse_kinematics(target_position, target_orientation)
print("Углы соединений:", joint_angles)

# Визуализация цепи
fig, ax = plot_utils.init_3d_figure()
my_chain.plot(my_chain.inverse_kinematics(target_position), ax, target=target_position)
plt.xlim(-0.1, 0.1)
plt.ylim(-0.1, 0.1)
plt.show()