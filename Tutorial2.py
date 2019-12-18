#libraries and shiiitt
import tensorflow as tf
from tensorflow import keras
import numpy as np

#importing dataset
data = keras.datasets.imdb

#splitting data into training and testing data
#num_words=10000 grabs only the 10000 most common words, eliminates fluff
#shrinks data set a little etc
(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=10000)

#index correlating words to their assigned integer
word_index = data.get_word_index()

##something to do with keywords or some weird shiiit
word_index = {k:(v+3) for k, v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

#somewthing or other to do with reversing the way the word and index is called
#so the data set can have integers instead of words......
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

#"fancy" tensor fucntion to trim review size to be even
#must make data into a form that ins consistent, this fucntion does this
train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding="post", maxlen=256)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index["<PAD>"], padding="post", maxlen=256)

#decodes integer encoded data, data is integer encoded for faster processing
def decode_review(text):
    return " ".join([reverse_word_index.get(i, "?") for i in text])

#defining our model
model = keras.Sequential()
model.add(keras.layers.Embedding(10000, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))

model.summary()

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

x_val = train_labels[:10000]
x_train = train_labels[10000:]

y_val = train_labels[:10000]
y_train = train_labels[10000:]

fitModel = model.fit(x_train, y_train, epochs=15, batch_size=512, validation_data=(x_val, y_val), verbose=1)

results = model.evaluate(test_data, test_labels)

print(results)