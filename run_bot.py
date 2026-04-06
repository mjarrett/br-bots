import bikeraccoon.bot as brbot
import sys

brbot.run(
    master_config_file='bot.credentials.json',
    bot_config_file=sys.argv[1],
    path='./output',
)
