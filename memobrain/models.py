from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Activation, Flatten, MaxPooling2D, Dropout
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet_v2 import ResNet50V2

def create_cnn(X):
    '''Create CNN & Compile'''
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), strides=(3, 3),
                    activation='sigmoid', padding ='same',
                    input_shape=X.shape[1:]))
    model.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))
    model.add(Conv2D(16, (3, 3), activation='sigmoid', strides=(3, 3), padding ='same'))
    model.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))
    model.add(Conv2D(8, kernel_size=(3,3), activation='sigmoid', strides = (3,3), padding ='same'))
    model.add(MaxPooling2D(pool_size=(1, 1), padding='valid'))
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy', 'Recall', 'Precision'])

    return model

def create_resnet50(X):
    '''Create ResNet50 & Compile'''
    base_model = ResNet50(
        include_top=False, weights=None,
        input_shape=X.shape[1:], pooling=None, classes=1)
    model = Sequential(base_model)
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy', 'Recall', 'Precision'])
    return model

def create_resnet50v2(X):
    '''Create ResNet50v2 & Compile'''
    base_model = ResNet50V2(
        include_top=False, weights=None,
        input_shape=X.shape[1:], pooling=None, classes=1, classifier_activation='sigmoid')
    model = Sequential(base_model)
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy', 'Recall', 'Precision'])
    return model

def create_vgg16(X):
    '''Create VGG16 & Compile'''
    base_model = VGG16(include_top=False,
                        weights=None,
                        input_shape=X.shape[1:],
                        pooling=None,
                        classes=1,
                        classifier_activation='sigmoid')
    model = Sequential(base_model)
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy', 'Recall', 'Precision'])

    return model

def create_vgg19(X):
    '''Create VGG19 & Compile'''
    base_model = VGG19(include_top=False,
                        weights=None,
                        input_shape=X.shape[1:],
                        pooling=None,
                        classes=1,
                        classifier_activation='sigmoid')
    model = Sequential(base_model)
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy', 'Recall', 'Precision'])

    return model

def model_fit(model, X_train, y_train, num_verbose):
    '''Fit Model with EarlyStopping'''
    es = EarlyStopping(monitor='loss',
                       min_delta=0,
                       patience=8,
                       verbose=0,
                       mode='auto',
                       restore_best_weights=True)

    history = model.fit(X_train, y_train,
                        epochs = 100,
                        batch_size = 32,
                        validation_split=0.2,
                        verbose=num_verbose,
                        callbacks = [es])

    return history, model
