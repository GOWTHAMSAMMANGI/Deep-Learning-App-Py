import numpy as np
from tensorflow.keras.datasets import mnist
from model import create_model

def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(-1, 784).astype('float32') / 255
    x_test = x_test.reshape(-1, 784).astype('float32') / 255
    return (x_train, y_train), (x_test, y_test)

def main():
    (x_train, y_train), (x_test, y_test) = load_data()
    
    model = create_model()
    model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test))
    
    model.save('mnist_model.h5')
    print("Model training complete and saved to mnist_model.h5")

if __name__ == "__main__":
    main()
