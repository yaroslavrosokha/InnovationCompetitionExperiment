from os import environ


SESSION_CONFIGS = [


    {
        'name': 'fullTest',
        'display_name': "Innovation Experiment (NoFeedback-Feedback)",
        'num_demo_participants': 2,
        'app_sequence': [
                 'App00_Consent',
                 'App01_PreExperimentQuestionnaire',
                 'App02_ExperimentIntroduction',
                 'App03_ExperimentNoFeedback',
                 'App04_ExperimentFeedback',
                 'App05_RiskAversionElicitation',
                 'App06_LossAversionElicitation',
                 'App07_SunkCostFallacyElicitation',
                 'App08_ExperimentSingleDM',
                 'App08_GritQuestionnaire',
                 'App09_BigFiveQuestionnaire',
                 'App10_InnovationQuestionnaire',
                 'App11_PayoffScreen',
                 'App12_PostExperimentQuestionnaire'
        ],
    },



]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

PARTICIPANT_FIELDS = ['expiryInstructions','expiryExperimentPart1',
                      'expiryExperimentPart2','correctQuiz',
                      'groupNumber','groupType']



SECRET_KEY = '123456789'

INSTALLED_APPS = ['otree']
