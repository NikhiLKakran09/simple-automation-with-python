import webbrowser as web
import wikipedia


topic = "criptography"
lines = 3
data = wikipedia.summary(topic,sentences = lines)
print(data)