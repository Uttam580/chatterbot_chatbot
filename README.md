![GitHub repo size](https://img.shields.io/github/repo-size/Uttam580/chatterbot_chatbot?style=plastic)
![GitHub language count](https://img.shields.io/github/languages/count/Uttam580/chatterbot_chatbot?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/Uttam580/chatterbot_chatbot?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/Uttam580/chatterbot_chatbot?color=red&style=plastic)



## chatterbot-chatbot

#### A web implementation of [ChatterBot](https://github.com/gunthercox/ChatterBot) using Flask.


**quick demo**

  ![demo_gif](https://github.com/Uttam580/chatterbot_chatbot/blob/master/demo.gif)


### What is chatbot:

A chatbot is an artificial intelligence-powered piece of software in a device (Siri, Alexa, Google Assistant etc), application, website or other networks that try to gauge consumer’s needs and then assist them to perform a particular task like a commercial transaction, hotel booking, form submission etc . 

Today almost every company has a chatbot deployed to engage with the users. Some of the ways in which companies are using chatbots are:

    * To deliver flight information

    * to connect customers and their finances

    * As customer support. The possibilities are (almost) limitless.

### chatterbot : 

ChatterBot is a library in python which generates responses to user input. It uses a number of machine learning algorithms to produce a variety of responses. It becomes easier for the users to make chatbots using the ChatterBot library with more accurate responses.


### How Does It work?

ChatterBot makes it easy to create software that engages in conversation. Every time a chatbot gets the input from the user, it saves the input and the response which helps the chatbot with no initial knowledge to evolve using the collected responses.
With increased responses, the accuracy of the chatbot also increases. The program selects the closest matching response from the closest matching statement that matches the input, it then chooses the response from the known selection of statements for that response.

I trained  based on  english greetings and conversations corpora.

        ```#created chatbot with name john 

        #SQLStorageAdapter which allows the chat bot to connect to SQL databases. By default, this adapter will create a SQLite database.

        english_bot = ChatBot("John", storage_adapter="chatterbot.storage.SQLStorageAdapter")

        trainer = ChatterBotCorpusTrainer(english_bot)#allows the chat bot to be trained using data from the ChatterBot dialog corpus.

        trainer.train("chatterbot.corpus.english")# trainning based on  english greetings and conversations corpora.```


### ```Language Independence```

The design of ChatterBot is such that it allows the bot to be trained in multiple languages. On top of this, the machine learning algorithms make it easier for the bot to improve on its own using the user’s input.


### Project Directory Tree

```
flask-chatterbot-master
├─ app.py
├─ demo.gif
├─ README.md
├─ requirements.txt
├─ static
│  ├─ css
│  │  └─ style.css
│  └─ js
│     └─ main.js
└─ templates
   └─ index.html

```

### Local Setup:
 1. Ensure that Python, Flask, SQLAlchemy, and ChatterBot are installed (either manually, or run `pip install -r requirements.txt`).
 2. Run *app.py* with `python app.py`.
 3. The demo will be live at [http://localhost:5000/](http://localhost:5000/)


 ###  Bug / Feature Request

If you find a bug (unable to initialize cudnn / or gave undesired results), kindly open an issue <a href = "https://github.com/Uttam580/chatterbot_chatbot/issues/new">here</a> by including your search query and the expected result.


 ### Resource: 

 https://chatterbot.readthedocs.io/en/stable/#


