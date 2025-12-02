# Thank yous
- Many thanks to the <a href="https://github.com/perezjln/gym-lowcostrobot">gym-lowcostrobot</a> project, which this repo has borrowed/inspired from to implement the Mujoco simulation and control of the the Koch arm. Specifically, the `assets` folder and gym environments are largely adapted from the original repo.

# Setup

You can clone the repo, make (and activate) a python conda virtual environment, and then do an editable install (with optional dependecies):

```
# Clone the repo and go into it.
git clone https://github.com/eric-rosen/lerobot_mujoco.git
cd lerobot_mujoco

# Make and activate conda environment.
conda create -n lerobot_mujoco python=3.10
conda activate lerobot_mujoco

# (Suggested) Install package with keyboard control
pip install -e .[keyboard]
# Or just vanilla install
pip install -e .
```

You're ready to play with robots :)

# Examples
## Keyboard teleop
Run the following example for keyboard teleop:

```
python src/lerobot_mujoco/examples/keyboard_teleop.py 
```

You'll see two windows pop up: 1) the robot render in a mujoco render, and 2) a small pygame window. If you click on the pygame window, you can push/hold the following buttons to control a (red) ghost gripper that represents the goal pose for the robot's end effector:
- w/a/s/d/e/q: 3D global position control for end effector. Hold these to move fast, or tap them for precision.
- g: toggle gripper open/close.
- c: toggle visualizing red gripper representing goal pose.
- r: reset env.
- z: quit.



# TODOS
- Put videos on the github repo readme
- add tests
- spell check
- make ASSETS_PATH use the import instead of dir path
- adjust camera so its convient for controlling directly
- add linting
- make it so that the speed of the command pose is adjustable.