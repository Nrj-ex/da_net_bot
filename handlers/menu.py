from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils import save_ids_message_for_delete, delete_messages
from loader import storage

from constants import YESNO


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /menu is issued."""

    await delete_messages(update, context)
    user = update.effective_user
    storage.add_user(user=user)
    messages_for_delete = []

    keyboard = [
        [InlineKeyboardButton('yes/no?', callback_data=YESNO)],
    ]

    message = await context.bot.send_message(chat_id=user.id,
                                             text='menu text',
                                             reply_markup=InlineKeyboardMarkup(keyboard))
    messages_for_delete.append(message)

    await save_ids_message_for_delete(context, *messages_for_delete)
