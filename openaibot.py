import openai

class ChatBot:
    def __init__(self):
        openai.api_key = "getyourkeyatopenaidotcom"

    def get_reposnse(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=3000,
                temperature=0.5
            ).choices[0].text
            return response
        except openai.error.APIError as e:
            # Handle API error here, e.g. retry or log
            print(f"OpenAI API returned an API Error: {e}")
            pass
        except openai.error.APIConnectionError as e:
            # Handle connection error here
            print(f"Failed to connect to OpenAI API: {e}")
            pass
        except openai.error.RateLimitError as e:
            # Handle rate limit error (we recommend using exponential backoff)
            print(f"OpenAI API request exceeded rate limit: {e}")
            pass

if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_reposnse("How are you today?")
    print(response)
