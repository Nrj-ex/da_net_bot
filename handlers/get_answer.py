from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import httpx


async def get_answer() -> dict:
    url = 'https://yesno.wtf/api'
    headers = {'User-Agent': 'httpx'}

    async with httpx.AsyncClient() as client:
        for _ in range(10):
            try:
                resp = await client.get(url=url, headers=headers)
                # {
                #     "answer": "no",
                #     "forced": false,
                #     "image": "https://yesno.wtf/assets/no/24-159febcfd655625c38c147b65e5be565.gif"
                # }
                if resp.status_code == 200 and resp.json().get('image') and resp.json().get('answer'):
                    return resp.json()

            except Exception:
                pass


async def yes_or_no(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = await get_answer()

    keyboard = [
        [InlineKeyboardButton('Задать вопрос!', url='https://t.me/da_da_net_net_bot?start=1')],
    ]

    await context.bot.send_video(
        chat_id=update.effective_user.id, caption=f'Вопрос: {update.effective_message.text}',
        video=answer.get('image'), reply_markup=InlineKeyboardMarkup(keyboard))
