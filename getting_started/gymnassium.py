!pip install gymnasium[toy_text] imageio
import numpy as np
import gymnasium as gym
import imageio
from IPython.display import Image
from gymnasium.utils import seeding

env = gym.make("Taxi-v3", render_mode='rgb_array')

env.np_random, _ = seeding.np_random(42)
env.action_space.seed(42)
np.random.seed(42)

max_actions = 100 

!pip install gymnasium[toy_text] imageio
import numpy as np
import gymnasium as gym
import imageio
from IPython.display import Image
from gymnasium.utils import seeding

env = gym.make("Taxi-v3", render_mode='rgb_array')

env.np_random, _ = seeding.np_random(42)
env.action_space.seed(42)
np.random.seed(42)

max_actions = 100 