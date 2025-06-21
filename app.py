from flask import Flask, request, render_template
import pickle

# Load tokenizer (vectorizer) and model
tokenizer = pickle.load(open('D:\Dibu\Course_Notes\Flask\Spam_classifier_model_deployment\model\cv.pkl', 'rb'))
model = pickle.load(open('D:\Dibu\Course_Notes\Flask\Spam_classifier_model_deployment\model\clf.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', text=None, result=None)

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('email')

    if not text:
        return render_template('home.html', text='', prediction='Please enter some text.')

    tokenized_text = tokenizer.transform([text])
    prediction_label = model.predict(tokenized_text)

    prediction = "Spam" if prediction_label[0] == 1 else "Not Spam"
    return render_template('home.html', text=text, prediction=prediction)

@aap.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json(force=True)
    text = data.get('email')

    if not text:
        return {'error': 'Please provide an email text.'}, 400

    tokenized_text = tokenizer.transform([text])
    prediction_label = model.predict(tokenized_text)

    prediction = "Spam" if prediction_label[0] == 1 else "Not Spam"
    return {'prediction': prediction}, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
