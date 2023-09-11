from gpt_session import gptSession

API_KEY = "YOUR API KEY HERE!"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

if __name__ == "__main__":
    session = gptSession(API_KEY, API_ENDPOINT)
    #chatting with gpt-4 api (using session -> gpt4 will remember the previous conversations [context feature])
    response = session.send_message("my names is arthur and you ?")
    print("1.response",response)
    response = session.send_message("what is the last question i asked you?")
    print("2.response",response)
    response = session.send_message("what was my name ?")
    print("3.response",response)
  
    #session.save_debug_as_file()

