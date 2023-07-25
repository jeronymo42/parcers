import speech_recognition as sr
import config
import telebot
import soundfile as sf

# Присваивание токена
bot = telebot.TeleBot(config.TOKEN)
transcriber = sr.Recognizer()

@bot.message_handler(content_types=["voice"])
def repeat_all_messages(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('new_file.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)
    data, samplerate = sf.read('new_file.ogg')
    sf.write('wav_file.wav', data, samplerate)

    with sr.AudioFile('wav_file.wav') as source:
        audio = transcriber.record(source)
        text = transcriber.recognize_sphinx(audio, language='rus')
        message.text = text
        bot.send_message(message.chat.id, message.text)
    
bot.polling(none_stop=True)