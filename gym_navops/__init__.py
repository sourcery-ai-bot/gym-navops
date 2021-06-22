#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from gym.envs.registration import register

from .config import EnvironmentConfig

"""
register(
    id='NavOps-v0',
    entry_point='gym_navops.envs:NavOpsEnv',
    kwargs={
        'worker_id': 0,
        'base_port': None,
        'seed': 0,
        'no_graphics': False,
        'override_path': None,
        '_build': 'NavOps',
        '_n': 2,
        '_group': False
    }
)

register(
    id='NavOpsDiscrete-v0',
    entry_point='gym_navops.envs:NavOpsEnv',
    kwargs={
        'worker_id': 0,
        'base_port': None,
        'seed': 0,
        'no_graphics': False,
        'override_path': None,
        '_build': 'NavOpsDiscrete',
        '_n': 2,
        '_group': False
    }
)
"""

register(
    id='NavOpsMultiDiscrete-v0',
    entry_point='gym_navops.envs:NavOpsEnv',
    kwargs={
        'build_path': None,
        'port': 9090
    }
)

"""
register(
    id='NavOpsMultiDiscrete-v1',
    entry_point='gym_navops.envs:NavOpsEnv',
    kwargs={
        'worker_id': 0,
        'base_port': None,
        'seed': 0,
        'no_graphics': False,
        'override_path': None,
        '_build': 'NavOpsMultiDiscrete',
        '_n': 1,
        '_group': False
    }
)

register(
    id='NavOpsMultiDiscrete-v2',
    entry_point='gym_navops.envs:NavOpsEnv',
    kwargs={
        'worker_id': 0,
        'base_port': None,
        'seed': 0,
        'no_graphics': False,
        'override_path': None,
        '_build': 'NavOpsMultiDiscrete',
        '_n': 3,
        '_group': True
    }
)
"""

"""
register(
    id='NavOpsDiscreteSkipFrame-v0',
    entry_point='gym_navops.envs:NavOpsEnv',
    kwargs={
        'worker_id': 0,
        'base_port': None,
        'seed': 0,
        'no_graphics': False,
        'override_path': None,
        'mock': False,
        '_discrete': True,
        '_skip_frame': True
    }
)
"""
