# Thank yous
- Many thanks to the <a href="https://github.com/perezjln/gym-lowcostrobot">gym-lowcostrobot</a> project, which this repo has borrowed/inspired from to implement the Mujoco simulation and control of the the Koch arm. Specifically, the `assets` folder and gym environments are largely adapted from the original repo.

# Setup

You can clone the repo, make (and activate) a python conda virtual environment, and then do an editable install:

```
# Clone the repo and go into it
git clone https://github.com/eric-rosen/lerobot_mujoco.git
cd lerobot_mujoco

# Make and activate conda environment
conda create -n lerobot_mujoco python=3.10
conda activate lerobot_mujoco

# Install package
pip install -e .
```

# TODOS
- Put videos on the github repo readme