import telegram
from datetime import datetime
import config

token = config.telegram_bot_token
id = config.chat_id
bot = telegram.Bot(token=token,)

date = datetime.today()

def iniciado(hora_inicio):
    bot.send_message(text=f'Buscador de resultados iniciado' , chat_id=id)
    unpin()
    funcionando(hora_inicio)
    pin()

def resultado_msg():
    bot.send_message(text='¡Resultado del Examen encontrado!', chat_id=id)

def resultado_imagen(pass_fail):
    bot.send_photo(id, photo=open('resultado.png', 'rb'), caption=f"Resultado: \n{pass_fail}")
    print("\nFoto enviada correctamente")

def update_funcionando(hora_actual):
    bot.editMessageText(message_id = funcionando_msg.message_id, text=f'Última Búsqueda: {hora_actual}', chat_id=id)

def funcionando(hora_actual):
    global funcionando_msg
    funcionando_msg = bot.send_message(text=f'Última Búsqueda: {hora_actual}', chat_id=id)

def fin():
    bot.send_message(text='Programa Finalizado', chat_id=id)

def pin():
    bot.pin_chat_message(chat_id = id, message_id = funcionando_msg.message_id)

def unpin():
    bot.unpin_all_chat_messages(chat_id = id)