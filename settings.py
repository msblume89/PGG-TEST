from os import environ


SESSION_CONFIGS = [
    dict(
        name='public_goods_simple',
        display_name="Public Goods Simple Loss-Game",
        app_sequence=['public_goods_simple', 'payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='public_goods_claim',
        display_name="Public Goods Claim-Game",
        app_sequence=['public_goods_claim', 'payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='public_goods_cooperation',
        display_name="Public Goods Cooperation-In-Loss-Cases-Game",
        app_sequence=['public_goods_cooperation', 'payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='public_goods_conditional',
        display_name="Public Goods Conditional-Contribution-Game",
        app_sequence=['public_goods_conditional', 'payment_info'],
        num_demo_participants=4,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.02, participation_fee=0.00, doc=""      #participation_fee hier negativ machen, wenn nicht mit Anfangsverlust ("beginningloss") gerechnet wird
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

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


SECRET_KEY = '1384922060924'

INSTALLED_APPS = ['otree']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "[Sammy]",
        "USER": "[Sammy]",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}