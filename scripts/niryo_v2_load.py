import mujoco
# import os
# import mujoco.viewer


# Path to your XML model
# model_path = '/home/xz2723/mujoco-ur5-model/niryo_one/model/niryo_step.xml'
model = mujoco.MjModel.from_xml_path('/home/xz2723/mujoco-ur5-model/niryo_one/model/niryo_step.xml')
data = mujoco.MjData(model)

print("Control the arm by modifying joint angles")

while True:
    mujoco.viewer.launch(model, data)