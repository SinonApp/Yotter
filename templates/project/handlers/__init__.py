from .echo import echo_handler

# Enable your handlers here.

enabled_handlers = {
    'echo': {
        'content_types': ['text'],
        'regexp': None,
        'commands': None,
        'chat_types': None,
        'func': None,
        'handler': echo_handler,
        'pass_bot': True
    }
}