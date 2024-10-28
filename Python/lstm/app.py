import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model("models/lstm_model.h5")

# Load the tokenizer
with open("data/IndiaUS.txt", 'r', encoding='utf-8') as myfile:
    mytext = myfile.read()

mytokenizer = Tokenizer()
mytokenizer.fit_on_texts([mytext])
total_words = len(mytokenizer.word_index) + 1

# Define maximum sequence length
max_sequence_len = max([len(seq) for seq in mytokenizer.texts_to_sequences(mytext.split('\n'))])

# Define a function to generate text
def generate_text(seed_text, next_words, max_sequence_len, model, tokenizer):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = np.argmax(model.predict(token_list), axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

# Streamlit app interface
st.title("LSTM Text Generation")

# Input text box for seed text
input_text = st.text_input("Enter seed text:", value="Joe Biden")

# Range slider for number of words to generate
predict_next_words = st.slider("Number of words to generate:", min_value=1, max_value=500, value=6)

# Button to generate text
if st.button("Generate Text"):
    generated_text = generate_text(input_text, predict_next_words, max_sequence_len, model, mytokenizer)
    st.text_area("Generated Text", value=generated_text, height=200)
