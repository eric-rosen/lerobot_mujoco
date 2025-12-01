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

# TODOS
- Put videos on the github repo readme
- add tests
- spell check
- add linting
- tutorial on how to run things
- make it so the keyboard teleop demo runs at a fixed hz (otherwise different computers may run at different speeds, etc.)