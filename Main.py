from aiogram import Bot, executor, Dispatcher
from aiogram.types import Message
from binance import AsyncClient

bot = Bot('5789191894:AAFIzzmrgsB0mVnbrPbO0wIJihVShxTonlk')
dispatcher = Dispatcher(bot)
binance_client = AsyncClient()


@dispatcher.message_handler(commands=['start'])
async def send_welcome(message: Message):
   await message.reply("Введите название токена: ")


@dispatcher.message_handler()
async def handle_coin_price(message: Message):		
	try:
		coin_name = str.upper(message.text)
		ticker_data = await binance_client.get_ticker(symbol = coin_name + 'USDT')
		usdt_ticker = ticker_data['lastPrice']
		await message.reply(coin_name +  ":\n" + usdt_ticker + " USDT")
	except Exception:
		await message.reply('Повторите попытку!')
	


if __name__ == '__main__':
	executor.start_polling(dispatcher)
