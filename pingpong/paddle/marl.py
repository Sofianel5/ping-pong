from ray.rllib.policy import TFPolicy
from abc import ABCMeta, abstractmethod
from collections import namedtuple
import gym
import numpy as np
from ray.rllib.env.multi_agent_env import MultiAgentEnv

class Config():
    """ Model related settings """
    ACTION_SET = ["SELL", "BUY"]
    MAX_CLASS_ID = 500
    NUM_PERIODS = 10 # later extend to 40 for sections
    MIN_POINTS = 0
    MAX_POINTS = 100
    EMPTY_SPACE_ID = -1
    CLASS_BIN_SIZE = 20

    """ RL related settings """
    STUDENT_OBSERVATION_SPACE = gym.spaces.Dict({
        "my_classes": gym.spaces.Box(low=EMPTY_SPACE_ID, high=MAX_CLASS_ID, shape=(NUM_PERIODS,)),
        "available_classes": gym.spaces.Box(low=EMPTY_SPACE_ID, high=MAX_CLASS_ID, shape=(CLASS_BIN_SIZE,))
    })

    STUDENT_ACTION_SPACE = gym.spaces.Dict({
        "trade_out": gym.spaces.Discrete(NUM_PERIODS-1), # the index of which class to trade out
        "trade_in": gym.spaces.Box(low=np.array([0,0]), high=np.array([CLASS_BIN_SIZE-1, NUM_PERIODS-1]), shape=(2,)), #  [intaking index, out index] 
        "do_nothing": gym.spaces.Discrete(2)
    })

    BUY_OBS_SPACE = gym.spaces.Discrete(2)
    SELL_OBS_SPACE = gym.spaces.Tuple((gym.spaces.Discrete(NUM_PERIODS), gym.spaces.Discrete(1)))

    BUY_ACTION_SPACE = gym.spaces.Discrete(1)
    SELL_ACTION_SPACE = gym.spaces.Discrete(1)


class BuyEnv(MultiAgentEnv):
    def __init__(self):
        self.action_space = Config.BUY_ACTION_SPACE
        self.observation_space = Config.BUY_OBS_SPACE

    def reset(self):
        pass 

    def step(self, action, agent):
        pass

class SellEnv(MultiAgentEnv):
    def __init__(self):
        self.action_space = Config.SELL_ACTION_SPACE 
        self.observation_space = Config.SELL_OBS_SPACE

    def reset(self):
        pass 

    def step(self, action, agent):
        pass
