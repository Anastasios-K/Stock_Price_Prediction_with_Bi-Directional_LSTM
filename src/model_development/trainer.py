import os
import pandas as pd
from src.config.load_conifg import Configurator
from keras_tuner.tuners import RandomSearch
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard, LearningRateScheduler, Callback


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
        self.__train_labels = train_labels
        self.__class_weights = class_weights
        self.__tuner_obj = tuner_object

    def execute_training(self):
        trained_model = self.__tuner_obj
        trained_model.search(
            x=self.__reshaped_train_data,
            y=self.__train_labels,
            verbose=1,
            epochs=self.__config.lstmGparams.epochs,
            batch_size=self.__config.lstmGparams.batchsiz,
            shuffle=False,
            validation_split=0.2,
            class_weight=self.__class_weights,
            callbacks=[
                EarlyStopping(
                    monitor='val_loss',
                    patience=self.__config.lstmGparams.earlystopping,
                    restore_best_weights=True
                ),
                TensorBoard(
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
            ]
        )
        return trained_model
