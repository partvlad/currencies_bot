"""Стартовая команда бота."""
from configs import log_configured
from telegram import Update
from telegram.ext import ContextTypes

logger = log_configured.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Логика команды /start."""
    if update.effective_chat is not None:
        message: str = (
            f'Показываю курс рубля специально для тебя,'
            f'{update.effective_chat.first_name}.'
            f'\n======<b>Доступные команды</b>======\n'
            f'- /start - приветственная информация\n'
            f'- /help - информация о функционале бота\n'
            f'- /courses - курсы всех или некоторых валют к рублю\n'
            f'- /sub - подписаться на рассылку'
            f'(с периодичностью в секундах, по выбранным валютам)\n'
            f'- /unsub - отписаться от рассылки'
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message, parse_mode='HTML',
        )
    else:
        logger.warning('Не получен ID чата при запросе /start.')
