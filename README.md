## 1. Obiettivi
---
- **Scopo:**
    Creare un'intelligenza artificiale in grado di:
    
    - Acquisire documenti in formato PDF
    - Analizzare il contenuto dei documenti
    - Classificarli automaticamente in categorie

## 2. Epica e User Stories
---
### Epica

- _Come utente voglio poter caricare documenti in formato PDF e farli classificare automaticamente in base al contenuto_

### User Story 1: Riconoscimento del contenuto

- _Il sistema deve riconoscere il testo per estrarre informazioni rilevanti_

### User Story 2: Classificazione dei documenti

- _Come utente voglio che il sistema classifichi automaticamente i documenti in categorie_

### User Story 3: Interfaccia

- _Come utente voglio un'interfaccia intuitiva_

## 5. Sprint
---
### Sprint 1

- **Obiettivi:**
    - Configurazione dell’ambiente di sviluppo (PyCharm)
    - Definizione della struttura (Python, ML, DB, Flask)

### Sprint 2

- **Attività:**
    - Progettazione e implementazione dei modelli di riconoscimento (Convolutional Neural Network -> audio, immagini - Recurrent Neural Network - Transformer -> traduzioni e generazione).
    - Creazione e preparazione del dataset per l’addestramento.
    - Test dei modelli.
    - (CNN https://www.ibm.com/think/topics/convolutional-neural-networks)
    - (RNN https://www.ibm.com/think/topics/recurrent-neural-networks)
    - (Transformer https://www.ibm.com/think/topics/transformer-model)

### Sprint 3

- **Attività:**
    - Addestramento dei modelli di classificazione
    - Integrazione del modulo di classificazione con il modulo di riconoscimento
    - Validazione dei risultati e miglioramento degli algoritmi

### Sprint 4

- **Attività:**
    - Sviluppo del front-end
    - Integrazione delle API


[https://www.docsumo.com/blogs/ocr/document-classification#:~:text=Document%20classification%20assigns%20a%20document,information%20helps%20us%20find%20information.]



https://huggingface.co/  per modelli
https://huggingface.co/docs/transformers/quicktour per far girare i modelli 


1. Documenti (circolari ad esempio)
	1. Scaricare tutte le circolari
	2. Fare batch che estragga il testo da ogni PDF
	3. Eliminare i PDF una volta estratto il testo

2. Da PDF a text
3. Da text cercare parole più comuni (token, es con regex)
4. Costruzione dataset (se token appare 1 volta scarta)
5. Riduzione di dimensionalità (riduzione numero di colonne, quelle che non incidono sul contenuto effettivo) in parallelo con il clustering (cerca classificazioni in base ai valori dei token)

#### Modelli
---
1. https://huggingface.co/prithivMLmods/MBERT-Context-Specifier
2. https://huggingface.co/E-MIMIC/inclusively-classification
3. https://huggingface.co/mayapapaya/Keyword-Extractor
4. https://huggingface.co/tabularisai/multilingual-sentiment-analysis
5. https://huggingface.co/BAAI/bge-reranker-v2-m3
6. https://github.com/FabrizioDeSantis/multi-label-text-classification-bert

#### Datasets (lo creo io con le circolari)
---
1. https://metatext.io/datasets/cc100-italian
2. https://huggingface.co/datasets/gsarti/clean_mc4_it
3. https://www.mdpi.com/2078-2489/13/5/228
4. https://paperswithcode.com/dataset/mldoc
5. https://github.com/laiguokun/xlu-data
6. https://paperswithcode.com/dataset/itacola
7. https://paperswithcode.com/dataset/italian-crime-news
8. https://paperswithcode.com/dataset/multilingual-top
9. https://paperswithcode.com/dataset/tilde-model-corpus
10. https://www.kaggle.com/datasets/alvations/old-newspapers?resource=download

#### Link utili
---
1. https://medium.com/@claude.feldges/text-classification-with-tf-idf-lstm-bert-a-quantitative-comparison-b8409b556cb3
2. https://www.klippa.com/en/blog/information/document-classification/
3. https://www.datacamp.com/tutorial/text-classification-python
4. https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/
5. https://medium.com/analytics-vidhya/nlp-tutorial-for-text-classification-in-python-8f19cd17b49e
6. https://medium.com/towards-data-science/naive-bayes-document-classification-in-python-e33ff50f937e
7. https://spotintelligence.com/2023/10/23/document-classification-python/
