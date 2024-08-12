import config
from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram.ext import (
    Application, CommandHandler, AIORateLimiter, CallbackQueryHandler, MessageHandler, filters, InlineQueryHandler
)

from handlers import start, help, menu, button_options, yes_or_no


def main() -> None:
    """Start the bot."""

    application = Application.builder().token(config.token).rate_limiter(
        AIORateLimiter(overall_max_rate=10, max_retries=3)).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, yes_or_no))

    application.add_handler(CallbackQueryHandler(button_options))

    application.run_polling()


if __name__ == "__main__":
    main()
