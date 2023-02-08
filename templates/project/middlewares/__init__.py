from .antiflood import AntifloodMiddleware

# Enable your middlewares here.

enabled_middlewares = {
    'antiflood': {
        'class': AntifloodMiddleware,
        'args': [2]
    }
}


[
    (AntifloodMiddleware, 2)
]