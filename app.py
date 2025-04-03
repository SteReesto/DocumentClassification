import os
from collections import Counter
import fitz
from flask import Flask, render_template, request
import DAO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['pdf_file']

        if file.filename.endswith('.pdf'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            text = read_pdf(file_path)
            tokenized = tokenize_words(text)
            most_common = find_common_words(tokenized)
            label = label_doc(tokenized)

            labeled_file = {
                "filename": file.filename,
                "label": label
            }

            if 'PCTO' in file.filename:
                labeled_file['label'] = 'PCTO'

            last_id = DAO.create_document(labeled_file)
            labeled_file['id'] = last_id


    return render_template('upload.html')


def read_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ''
    for page in doc:
        text += page.get_text().lower().replace("’", " ").replace('"', ' ')

    doc.close()

    return text


def tokenize_words(text):
    single_words = text.split()
    to_be_removed = ['istituto', 'tecnico', 'mario', 'delpozzo', 'degli', 'della', 'delle', 'nella', 'nelle', 'cuneo',
                     'hanno', 'sulla', 'sulle', 'lunedi', 'lunedì', 'martedi', 'martedì', 'mercoledi', 'mercoledì',
                     'giovedi', 'giovedì', 'venerdi', 'venerdì', 'sabato', 'domenica']

    ''' filtra le parole che non sono presenti nella lista to_be_removed e ritorna solo quelle più lunghe di 4 caratteri
    e alfabetiche '''

    filtered_words = [word for word in [word for word in single_words if word not in to_be_removed] if
                      len(word) > 4 and word.isalpha()]

    return filtered_words


def find_common_words(data):
    word_count = Counter(data)
    return word_count.most_common(50)


def label_doc(list_of_words):
    words_to_be_found = [
        ('assemblea', 'assemblee'), ('assemblee', 'assemblee'), ('orario', 'orari'), ('orari', 'orari'),
        ('consiglio', 'consigli'), ('consigli', 'consigli'), ('intervallo', 'intervalli'), ('PCTO', 'PCTO'),
        ('pcto', 'PCTO'),
        ('intervalli', 'intervalli'), ('attività', 'attività'), ('vacanza', 'vacanze'), ('vacanze', 'vacanze'),
        ('esame', 'esami'), ('esami', 'esami'), ('prime', 'prime'), ('prima', 'prime'), ('seconde', 'seconde'),
        ('seconda', 'seconde'),
        ('terze', 'terze'), ('terza', 'terze'), ('quarte', 'quarte'), ('quarta', 'quarte'),
        ('quinte', 'quinte'), ('quinta', 'quinte'), ('sciopero', 'scioperi'), ('scioperi', 'scioperi')
    ]

    label = [label for word, label in words_to_be_found if word in list_of_words]

    if label:
        return label[0]
    else:
        return 'altro'


if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads/')
    app.run()
