import bikeraccoon.bot as brbot
import logging
from logging.handlers import RotatingFileHandler
import os
import sys

import bikeraccoon as br
br.APIBase.api_base_url = 'https://apiprod.raccoon.bike'

os.makedirs('logs', exist_ok=True)

log_format = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

file_handler = RotatingFileHandler(
    'logs/run_bot.log',
    maxBytes=5 * 1024 * 1024,  # 5 MB
    backupCount=5,
)
file_handler.setFormatter(log_format)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_format)

logging.basicConfig(
    level=logging.INFO,
    handlers=[file_handler, stream_handler],
)
logger = logging.getLogger(__name__)

bot_config = sys.argv[1]
bot_name = os.path.splitext(os.path.basename(bot_config))[0]
logger.info('Starting bot: %s', bot_config)

try:
    brbot.run(
        master_config_file='bot.credentials.json',
        bot_config_file=bot_config,
        path=f'./output/{bot_name}',
    )
    logger.info('Bot finished: %s', bot_config)
except Exception:
    logger.exception('Bot failed: %s', bot_config)
    sys.exit(1)
