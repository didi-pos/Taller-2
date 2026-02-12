# run_env.py
import os
import time
import gym
import humanoid_gym

def main():
    robot = os.getenv("ROBOT_ENV", "pepper")
    env_id = f"{robot}-v0"
    print("Loading environment:", env_id)
    env = gym.make(env_id)
    obs = env.reset()
    print("Running:", env)
    try:
        while True:
            obs, reward, done, info = env.step(env.action_space.sample())
            if done:
                obs = env.reset()
            # reduce CPU spin
            time.sleep(0.02)
    except KeyboardInterrupt:
        print("Interrupted, exiting.")

if __name__ == "__main__":
    main()
