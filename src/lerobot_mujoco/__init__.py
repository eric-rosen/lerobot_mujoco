import os

from gymnasium.envs.registration import register

register(
    id="LiftCube-v0",
    entry_point="lerobot_mujoco.envs:LiftCubeEnv",
)

register(
    id="PickPlaceCube-v0",
    entry_point="lerobot_mujoco.envs:PickPlaceCubeEnv",
)

register(
    id="PushCube-v0",
    entry_point="lerobot_mujoco.envs:PushCubeEnv",
)

register(
    id="ReachCube-v0",
    entry_point="lerobot_mujoco.envs:ReachCubeEnv",
)

register(
    id="StackTwoCubes-v0",
    entry_point="lerobot_mujoco.envs:StackTwoCubesEnv",
)

register(
    id="PushCubeLoop-v0",
    entry_point="lerobot_mujoco.envs:PushCubeLoopEnv",
)