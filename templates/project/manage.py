from config import settings
import handlers
import middlewares
import logging
import telebot
import argparse

parser = argparse.ArgumentParser(prog = 'manage.py', description = 'Manager for Yotter')
parser.add_argument('command')
args = parser.parse_args()

if args.command == 'runbot':
    logger = telebot.logger

    logging_levels = {
        'info': logging.INFO,
        'debug': logging.DEBUG,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL,
    }

    telebot.logger.setLevel(logging_levels[settings.LOGGIN_LEVEL])
    bot = telebot.TeleBot(settings.BOT_TOKEN, use_class_middlewares=settings.MIDDLEWARED_ENABLED, parse_mode=settings.DEFAULT_PARSE_MODE)

    if settings.MIDDLEWARED_ENABLED:
        for middleware in middlewares.enabled_middlewares:
            bot.setup_middleware(
                middlewares.enabled_middlewares[middleware]['class'](bot, *middlewares.enabled_middlewares[middleware]['args'])
            )

    if settings.CUSTOM_FILTERS != []:
        for filter in settings.CUSTOM_FILTERS:
            bot.add_custom_filter(filter(bot))

    for handler in handlers.enabled_handlers:
        handler = handlers.enabled_handlers[handler]
        if handler['content_types'] is not None:
            bot.register_message_handler(handler['handler'],
                content_types=handler['content_types'],
                chat_types=handler['chat_types'],
                pass_bot=handler['pass_bot']
            )
        elif handler['regexp'] is not None:
            bot.register_message_handler(handler['handler'],
                regexp=handler['regexp'],
                chat_types=handler['chat_types'],
                pass_bot=handler['pass_bot']
            )
        elif handler['commands'] is not None:
            bot.register_message_handler(handler['handler'],
                commands=handler['commands'],
                chat_types=handler['chat_types'],
                pass_bot=handler['pass_bot']
            )
        elif handler['func'] is not None:
            bot.register_message_handler(handler['handler'],
                func=handler['func'],
                chat_types=handler['chat_types'],
                pass_bot=handler['pass_bot']
            )

    if settings.POLLING_ENABLE:
        if settings.POLLING_INF:
            bot.infinity_polling(
                timeout=settings.POLLING_TIMEOUT,
                allowed_updates=settings.POLLING_ALLOW_UPDATES,
                skip_pending=settings.POLLING_SKIP_PENDING
            )
        else:
            bot.polling(
                timeout=settings.POLLING_TIMEOUT,
                allowed_updates=settings.POLLING_ALLOW_UPDATES,
                skip_pending=settings.POLLING_SKIP_PENDING
            )