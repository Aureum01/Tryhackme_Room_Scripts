# ... (previous imports) ...
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ... (previous code) ...

# Load the trained neural network model
model = load_model('your_trained_model.h5')

# Initialize the tokenizer with the same parameters used during training
tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')

# ... (inside the loop) ...

# Preprocess the error message
error_message_list = [error_message]
tokenized_error_message = tokenizer.texts_to_sequences(error_message_list)
padded_error_message = pad_sequences(tokenized_error_message, maxlen=100, padding='post')

# Predict the probability of a successful login attempt
probability = model.predict(padded_error_message)[0][0]

# Print the probability along with the error message
print(f"{username} - Error message: {error_message} - Probability: {probability:.2f}")
