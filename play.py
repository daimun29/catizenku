from telegram import Update, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Setup logging
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

# Perintah /start untuk memulai game
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    web_app_url = "https://t.me/catizenbot"  # Ganti dengan URL game mini apps Anda

    # Kirim tombol untuk membuka mini apps
    keyboard = [[
        InlineKeyboardButton("Play Catizen Game", web_app={"url": web_app_url})
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        f"Hi {user.first_name}! Klik tombol di bawah untuk bermain Catizen Game!",
        reply_markup=reply_markup,
    )

# Fungsi untuk menerima data dari game
def handle_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data  # Data dari game dikirim ke sini

    # Contoh: Data skor dikirim dari mini apps
    if "score" in data:
        score = int(data.split("=")[1])  # Ambil skor dari data
        query.answer(f"Skor kamu: {score}!")

# Fungsi utama
def main():
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    updater = Updater(TOKEN)

    # Daftar perintah
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(handle_callback))

    # Jalankan bot
    logging.info("Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
