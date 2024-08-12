from telegram import Update
from telegram.ext import ContextTypes
from handlers.menu import menu
from handlers.help import help
from handlers.get_answer import yes_or_no
from constants import MENU, HELP, YESNO


async def button_options(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    await query.answer()

    # if query.data == MENU:
    #     await menu(update, context)
    #
    # elif query.data == HELP:
    #     await help(update, context)

    if query.data == YESNO:
        await yes_or_no(update, context)
