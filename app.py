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
    convo = model.start_chat(history=[])
    convo.send_message(message)
    return jsonify({'response': convo.last.text})


#to use as assist
@app.route('/assist', methods=['POST'])
def assist():
    message = request.json['message']
    convo = model.start_chat(history=[])
    convo.send_message(message)
    return jsonify({'response': convo.last.text})



if __name__ == '__main__':
    app.run(debug=True)
