import os
import pandas as pd
import numpy as np
from src.config.load_conifg import Configurator
import tensorflow as tf
from keras_tuner.tuners import RandomSearch
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard, ModelCheckpoint


class Trainer:
    def __init__(
            self,
            config: Configurator,
            unique_id: str,
            reshaped_train_data: pd.DataFrame,
            train_labels: pd.Series,
            class_weights: dict,
            tuner_object: RandomSearch
    ):
        self.__config = config
        self.__unique_id = unique_id
        self.__reshaped_train_data = reshaped_train_data
        self.__train_labels = np.array(train_labels)
        self.__class_weights = class_weights
        self.__tuner_obj = tuner_object

    def __create_earlystopping_callback(self) -> EarlyStopping:
        """ Create Earlystopping Callback to control the learnig process and avoid overfitting. """
        earlystopping = EarlyStopping(
            monitor='val_loss',
            patience=self.__config.lstmGparams.earlystopping,
            restore_best_weights=True,
            mode="min"
        )
        return earlystopping

    def __create_tensorboard_callback(self) -> TensorBoard:
        """ Create TensorBoard Callback to track model the leanring process and hyper parameter tuning. """
        tesnorboard = TensorBoard(
                    log_dir=os.path.join(
                        *self.__config.dirs2make.hyperparams,
                        self.__config.modelname.modelname + self.__unique_id
                    ),
                    histogram_freq=1,
                    embeddings_freq=1,
                    write_graph=True,
                    update_freq='epoch',
                    profile_batch=0
                )
        return tesnorboard

    def __create_modelcheckpoint_callback(self) -> ModelCheckpoint:
        """
        Create ModelCheckpoint to track/save learning progress.
        So, we can restore the model with all features applied into the last epoch and batch.
        """
        modelcheckpoint = ModelCheckpoint(
            filepath=os.path.join(
                *self.__config.dirs2make.models,
                self.__config.modelname.modelname + self.__unique_id,
                "checkpoint.h5"
            ),
            save_weights_only=False,
            monitor='loss',
            mode='min',
            save_best_only=True,
            save_freq=1
        )
        return modelcheckpoint

    def execute_training(self) -> RandomSearch:
        """
        Execute training process.
        Split the training set into training and validation set.
        Incorporates all the above Callbacks.
        """
        trained_model = self.__tuner_obj
        trained_model.search(
            x=self.__reshaped_train_data,
            y=tf.keras.utils.to_categorical(y=self.__train_labels),
            verbose=1,
            epochs=self.__config.lstmGparams.epochs,
            batch_size=self.__config.lstmGparams.batches,
            shuffle=False,
            validation_split=0.2,
            class_weight=self.__class_weights,
            callbacks=[
                self.__create_modelcheckpoint_callback()
            ]
        )
        return trained_model
