"""
Reward Base Class
"""

from __future__ import annotations
from abc import abstractmethod


class Reward:
    """
    Abstract class for reward provider.
    """

    @abstractmethod
    def reward(self, obs, action):
        """Calculate reward for current state

        Raises:
            NotImplementedError
        """
        raise NotImplementedError()

    def reset(self):
        """
        Reset reward provider
        """
        pass


class DefaultReward(Reward):
    """
    Default reward provider.
    """

    def reward(self, obs, action):
        """
        Return constant 0.01 reward
        """
        return 0.001, False