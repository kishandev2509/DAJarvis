#open AI
import openai
from dotenv import load_dotenv

with open(r"api.txt","r") as fileopen:
    API = fileopen.read()

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def chat_log():
    with open(r"database\chat_log.txt","r") as f:
        chat_log = f.read()
        chat_log = chat_log[-4000:]
        # print(chat_log)
    return chat_log



def getResponse(question):
    response = completion.create(
        model = "text-davinci-002", 
        prompt = f"{chat_log()}\nYou : {question} \nJarvis : ",
        temperature = 0,
        max_tokens = 1024,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0
    )
    answer = response.choices[0].text.strip()
    chat_log_update = f"\nYou : {question} \nJarvis : {answer}"
    fileLog = open(r"database\chat_log.txt","a")
    fileLog.write(chat_log_update)
    fileLog.close()
    return answer

if __name__ == "__main__":
    while True:
        inputs = input("Enter :")
        print(getResponse(inputs))

