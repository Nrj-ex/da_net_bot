from telegram import Update
from telegram.ext import ContextTypes


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""

    user = update.effective_user
    help_text = f"""Задайте боту вопрос на который можно ответить да или нет!"""

    await context.bot.send_message(chat_id=user.id, text=help_text)
