from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

#created chatbot with name john 
#SQLStorageAdapter which allows the chat bot to connect to SQL databases. By default, this adapter will create a SQLite database.
english_bot = ChatBot("John", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)#allows the chat bot to be trained using data from the ChatterBot dialog corpus.
trainer.train("chatterbot.corpus.english")# trainning based on  english greetings and conversations corpora 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
