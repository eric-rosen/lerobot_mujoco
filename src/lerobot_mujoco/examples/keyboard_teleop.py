import argparse
import gymnasium as gym
import lerobot_mujoco
import pygame
import numpy as np
import sys
import time

# gripper actions will be sticky, so last_gripper_state is last direction
sticky_gripper_action = 0

# Single function to read keys AND decide action/reset
def get_keyboard_action(env, action_mode):
    global sticky_gripper_action
    pressed = []


    # For keys that are held down
    keys = pygame.key.get_pressed()

    shift_pressed = keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]


    # For keys that pressed once (toggle)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                pressed.append("C")
                # toggle transparency
                for idx in [5,6]:
                    env.unwrapped.model.geom(f'sync_link_{idx}').rgba[-1] = 1 - env.unwrapped.model.geom('sync_link_6').rgba[-1]


            # f to toggle sticky gripper direction
            if event.key == pygame.K_f:
                pressed.append("F")
                if sticky_gripper_action == 0:
                    sticky_gripper_action = -0.1
                else:
                    sticky_gripper_action *= -1
            
            # Reset the environment if R is pressed
            if event.key == pygame.K_r:
                pressed.append("R")
                if shift_pressed:
                    env.unwrapped.reset_ee_pos_target()
                else:
                    env.reset()
                return [0, 0, 0, 0], pressed
            

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exist()

    if keys[pygame.K_z]:
        sys.exit()
        
    if action_mode == "ee":
        # x,y,z position + (g)ripper state
        x = y = z = 0

        # WASD movement
        if keys[pygame.K_w]:
            y = -1; pressed.append("W")
        elif keys[pygame.K_s]:
            y = 1; pressed.append("S")

        if keys[pygame.K_a]:
            x = 1; pressed.append("A")
        elif keys[pygame.K_d]:
            x = -1; pressed.append("D")

        if keys[pygame.K_q]:
            z = 1; pressed.append("Q")
        elif keys[pygame.K_e]:
            z = -1; pressed.append("E")

        return np.array([x, y, z, sticky_gripper_action]), pressed


def do_env_sim(task : str, action_mode : str):
    pygame.init()
    window = pygame.display.set_mode((200, 200))
    font = pygame.font.SysFont("consolas", 20)

    env = gym.make(
        task,
        observation_mode="state",
        render_mode="human",
        action_mode=action_mode,
        reward_type="dense"
    )
    env.reset()

    sim_dt = env.unwrapped.model.opt.timestep 

    last_time = 0

    while True:
        cur_time = time.time()
        if cur_time - last_time >= sim_dt:
            last_time = cur_time
            action, pressed_keys = get_keyboard_action(env, action_mode)

            observation, reward, terminated, truncated, info = env.step(action)

            # Draw pressed keys into pygame window
            window.fill((30, 30, 30))
            msg = "Keys: " + (" ".join(pressed_keys) if pressed_keys else "-")
            text_surface = font.render(msg, True, (255, 255, 255))
            window.blit(text_surface, (10, 80))
            pygame.display.flip()

            if terminated:
                env.reset()


from enum import Enum

class ActionMode(Enum):
    EE = "ee"
    JOINT = "joint"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Keyboard teleoperation for robot control")
    parser.add_argument("--task", choices=["pushcube", "liftcube"], default="pushcube",
                        help="Task to run (default: liftcube)")
    args = parser.parse_args()

    task_map = {
        "pushcube": "PushCube-v0",
        "liftcube": "LiftCube-v0",
    }
    task = task_map[args.task]
    action_mode = ActionMode.EE
    print("\n============ Keyboard Controls ============\n" \
    "w/a/s/d/e/q: 3D global position control for end effector. Hold these to move fast, or tap them for precision.\n" \
    "f: toggle gripper open/close.\n" \
    "c: toggle visualizing red gripper representing goal pose.\n"\
    "r: reset env.\n" \
    "z: quit.\n")
    do_env_sim(task, action_mode.value)