from ray.rllib.policy import TFPolicy
from abc import ABCMeta, abstractmethod
from collections import namedtuple
import gym
import numpy as np
from ray.rllib.env.multi_agent_env import MultiAgentEnv
from .models import Student

class Config():
    """ Model related settings """
    ACTION_SET = ["SELL", "BUY"]
    MAX_CLASS_ID = 500
    NUM_PERIODS = 10 # later extend to 40 for sections
    MIN_POINTS = 0
    MAX_POINTS = 100
    EMPTY_SPACE_ID = -1
    CLASS_BIN_SIZE = 20
    subject = Student

    BUY_OBS_SPACE = gym.spaces.Discrete(2) # (period, points) + current schedule
    SELL_OBS_SPACE = gym.spaces.Tuple((gym.spaces.Discrete(NUM_PERIODS), gym.spaces.Discrete(1))) # [(period, points) for class in classes)] + [(period, points) of highest bidding]

    BUY_ACTION_SPACE = gym.spaces.Discrete(1) # points
    SELL_ACTION_SPACE = gym.spaces.Discrete(1) # period 

def choose_env(worker_index, vector_index_):
    pass


class AssignmentEnv(MultiAgentEnv):
    def __init__(self, env_config):
        self.env = gym.make(choose_env(env_config.worker_index, env_config.vector_index))
        self.action_space = self.env.action_space 
        self.observation_space = self.env.observation_space 
        
    def with_agent_groups(self, groups, obs_space=None, act_space=None):
        pass
    
    def reset(self):
        return self.env.reset() 
    
    def step(self, action):
        return self.env.step(action)
    
class BuyEnv(MultiAgentEnv):
    def __init__(self):
        self.action_space = Config.BUY_ACTION_SPACE
        self.observation_space = Config.BUY_OBS_SPACE

    def reset(self):
        pass # return dict of {agent: obs space,...}
    
    def get_subject(self, agent_str):
        config.subject.objects.get(pk=agent_str[2:])
    
    def _obs_space(self):
        pass

    def step(self, action, agent):
        pass

class SellEnv(MultiAgentEnv):
    def __init__(self):
        self.action_space = Config.SELL_ACTION_SPACE 
        self.observation_space = Config.SELL_OBS_SPACE
        self.agents = []

    def reset(self):
        pass 

    def step(self, action, agent):
        pass
