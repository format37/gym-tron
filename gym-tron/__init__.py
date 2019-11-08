from gym.envs.registration import register

register(
    id='lex-tron',
    entry_point='gym-tron.envs:LexEnv',
)