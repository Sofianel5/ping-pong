from rllib.policy.policy import TFPolicy
from abc import ABCMeta, abstractmethod
from collections import namedtuple
import gym
import numpy as np
from rllib.env.multi_agent_env import MultiAgentEnv

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

class StudentEnv(MultiAgentEnv):
    def __init__(self):
        self.action_space = Config.STUDENT_ACTION_SPACE # plus one for do nothing
        self.observation_space = Config.STUDENT_OBSERVATION_SPACE

    def reset(self):
        pass 

    def step(self, action, agent):
        pass

class StudentPolicy(TFPolicy):
    pass