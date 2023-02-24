import os
import numpy as np
import pandas as pd
from src.interface.interface import Builder
from src.config.load_conifg import Configurator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense, Dropout, Flatten, BatchNormalization
from tensorflow.keras.initializers import GlorotUniform, Zeros, Orthogonal
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import BinaryCrossentropy, CategoricalCrossentropy
from tensorflow.keras.metrics import AUC, Precision, Recall
from keras_tuner.tuners import RandomSearch


class LstmBuilder(Builder):

    def __init__(
            self,
            config: Configurator,
            unique_id: str,
            train_data: pd.DataFrame,
            test_data: pd.DataFrame
    ):
        self.__config = config
        self.__unique_id = unique_id
        self.__train_data = train_data
        self.__test_data = test_data
        self.reshaped_tr_data = None
        self.reshaped_ts_data = None
        self._reshape_data()
        self.keras_tuner_model = self._initialise_tuner()
        print(type(self._build_model))

    def _reshape_data(self) -> None:
        """
        Reshape train and test data based on a window length which is set in configuration file.
        Tensorflow LSTM a 3D tensor with shape [batch, timesteps, feature].
        """
        window = self.__config.forecasthorizon.forcasthorizon
        windowed_train_dfs = list(self.__train_data.rolling(window))[window:]
        windowed_test_dfs = list(self.__test_data.rolling(window))[window:]
        self.reshaped_tr_data = np.array(windowed_train_dfs)
        self.reshaped_ts_data = np.array(windowed_test_dfs)

    def _build_model(self, hp) -> None:
        """
        Build Tensorfow LSTM model.
        The hp parameter is used by Keras Tuner only.
        So, we pass the whole method to Keras Tuner later in this script.
        The mothod initialises all the hyper parameters which are set in the configuration file.
        The method also incorporates the loss fucntion, optimiser and metrics.
        """
        # Load general and hyper parameters
        gparams = self.__config.lstmGparams
        hparams = self.__config.lstmHparams
        # set initialisation
        kernel_init = GlorotUniform(seed=gparams.seed)
        recurrent_init = Orthogonal(seed=gparams.seed)
        bias_init = Zeros()
        # build the lstm model
        model = Sequential()
        # prepare haper parameters
        lstm_units = hp.Int(
            "lstm_units",
            min_value=hparams.lstmunitsmin,
            max_value=hparams.lstmunitsmin,
            step=hparams.lstmunitstep
        )
        dense_units = hp.Int(
            "dense_units",
            min_value=hparams.denseunitsmin,
            max_value=hparams.denseunitsmax,
            step=hparams.denseunitstep
        )
        drop_out_values = hp.Choice(
            "drop out values",
            values=np.linspace(
                start=hparams.dropoutmin,
                stop=hparams.dropoutmax,
                num=hparams.dropoutstep,
                dtype=float).tolist()
        )
        lr_values = hp.Choice(
            "learning rate values",
            values=np.linspace(
                start=hparams.lrmin,
                stop=hparams.lrmax,
                num=hparams.lrstep,
                dtype=float).tolist()
        )
        # add layers into the model
        model.add(LSTM(
            name="LSTM_1",
            units=lstm_units,
            return_sequences=False,
            input_shape=self.reshaped_tr_data.shape[1:],
            activation=gparams.actfunc,
            recurrent_activation=gparams.reccactfunc,
            kernel_initializer=kernel_init,
            recurrent_initializer=recurrent_init
        ))

        model.add(Dropout(
            name="DropOut_1",
            rate=drop_out_values,
            seed=gparams.seed
        ))

        model.add(Dense(
            name="Dense_1",
            units=dense_units,
            use_bias=True, kernel_initializer=kernel_init,
            bias_initializer=bias_init,
            activation=gparams.densactfunc
        ))
        model.add(Dense(
            units=3,
            use_bias=True,
            kernel_initializer=kernel_init,
            bias_initializer=bias_init,
            activation=gparams.classactfunc
        ))

        model.compile(
            optimizer=Adam(learning_rate=lr_values),
            loss=CategoricalCrossentropy(),
            metrics=[
                AUC(name="AUC", curve="PR", from_logits=True),
                Precision(name="precision"),
                Recall(name="recall")
            ]
        )
        return model

    def _count_max_trials(self) -> int:
        """ Count the maximum possible combinations given the hyper parameters."""
        hparams = self.__config.lstmHparams
        count_lstm = np.arange(
            start=hparams.lstmunitsmin,
            stop=hparams.lstmunitsmax + 1,
            step=hparams.lstmunitstep
        )
        count_dense = np.arange(
            start=hparams.denseunitsmin,
            stop=hparams.denseunitsmax + 1,
            step=hparams.denseunitstep
        )
        count_drop_out = np.linspace(
            start=hparams.dropoutmin,
            stop=hparams.dropoutmax,
            num=hparams.dropoutstep,
            endpoint=True
        )
        count_lr_values = np.linspace(
            start=hparams.lrmin,
            stop=hparams.lrmax,
            num=hparams.lrstep,
            endpoint=True
        )
        trials = (len(count_lstm) *
                  len(count_dense) *
                  len(count_drop_out) *
                  len(count_lr_values))
        print(f"The maximum trials are: {trials}")
        return trials

    def _initialise_tuner(self) -> RandomSearch:
        """ Initialise Keras Tuner. """
        tuner = RandomSearch(
            hypermodel=self._build_model,
            objective="val_loss",
            max_trials=self._count_max_trials(),
            project_name=self.__config.modelname.modelname + self.__unique_id,
            # overwrite=True,
            directory=os.path.join(
                *self.__config.dirs2make.models,
                self.__config.modelname.modelname + self.__unique_id
            ),
            seed=self.__config.lstmGparams.seed
        )
        tuner.search_space_summary(extended=True)
        return tuner
