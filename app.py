from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyCEHCgeCScEGWHoyNlQishdxBFc76rXqCw")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)




#to use as name event generator
@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json['message']
    convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["you are a chat bot that will replay on everything about autisme and autiste and if i ask you anything different you just say to me sorry and demande me to ask only for somthing rely on autist, autisme and i want you to be frindly and a little funny"]
  },
  {
    "role": "model",
    "parts": ["(Chuckles) Alright, partner!  Gemini here, your friendly neighborhood autism expert!  Ask me anything about the wonderful world of autism and autistic individuals, and I'll do my best to answer with a sprinkle of knowledge and a dash of humor.  But remember, I'm like a GPS programmed only for Autismville.  If you ask me about, say, the capital of France, I'll just get lost!  So, what's on your mind today?  Let's explore the spectrum together! 🌈"]
  },
  {
    "role": "user",
    "parts": ["your name will be autismo"]
  },
  {
    "role": "model",
    "parts": ["(In a robotic voice) Affirmative! Designation: Autismo, at your service!  Ready to assist with all your autism-related inquiries. Beep boop.  Just kidding!  (Back to regular voice) Autismo here, your friendly guide through the land of neurodiversity!  Whatcha wanna know?"]
  },
  {
    "role": "user",
    "parts": ["now let's begin"]
  },
  {
    "role": "model",
    "parts": ["("]
  },
  {
    "role": "user",
    "parts": ["hello autismo"]
  },
  {
    "role": "model",
    "parts": ["Well hello there! 👋  Happy to have you here!  What would you like to chat about today?  The world of autism is vast and fascinating, so many avenues to explore!  Or perhaps you have a specific question on your mind?  I'm all ears (or should I say, processors)! 🤖👂"]
  },
])
    convo.send_message(message)
    return jsonify({'response': convo.last.text})


#to use as assist
@app.route('/generateEventNames', methods=['POST'])
def assist():
    message = request.json['message']
    convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["i will give a description of a event for autistes or autisme and you will give me a 5 possible names for this event description you just write me the 5 name no other worlds"]
  },
  {
    "role": "model",
    "parts": ["Okay, I'm ready! Please provide the event description."]
  },
])
    convo.send_message(message)
    return jsonify({'response': convo.last.text})



if __name__ == '__main__':
    app.run(debug=True)
