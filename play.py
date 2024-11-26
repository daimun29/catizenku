from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
import logging

# Setup logging
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

# Perintah /start untuk memulai game
async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    web_app_url = "https://example.com/catizen-game"  # Ganti dengan URL game mini apps Anda

    # Kirim tombol untuk membuka mini apps
    keyboard = [[
        InlineKeyboardButton("Play Catizen Game", web_app={"url": web_app_url})
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Hi {user.first_name}! Klik tombol di bawah untuk bermain Catizen Game!",
        reply_markup=reply_markup,
    )

# Fungsi untuk menerima data dari game
async def handle_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data  # Data dari game dikirim ke sini

    # Contoh: Data skor dikirim dari mini apps
    if "score" in data:
        score = int(data.split("=")[1])  # Ambil skor dari data
        await query.answer(f"Skor kamu: {score}!")

# Fungsi utama
def main():
    TOKEN = "7690148280:AAGkcB7_Pdz9fKyi9MHkTFFHSDwg6xl5B3s
    
    # Menggunakan Application di versi terbaru
    application = Application.builder().token(TOKEN).build()

    # Daftar perintah
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_callback))

    # Jalankan bot
    logging.info("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
