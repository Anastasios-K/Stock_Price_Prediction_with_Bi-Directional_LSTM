import mlflow
import keras.backend as keras_back


class Tracker:
    def __init__(self,
                 best_models,
                 config,
                 tracking_info,
                 unique_id,
                 prediction_metrics
):
        self.__best_models = best_models
        self.__config = config
        self.__tracking_info = tracking_info
        self.__unique_id = unique_id
        self.__prediction_metrics = prediction_metrics

    def __track_hyper_params(self) -> None:
        """ Trach hyeper parameters. """
        best_models = self.__best_models
        for indx in range(len(best_models)):
            model = best_models[indx]
            mlflow.log_param(f"model_{indx} learning_rate", str(keras_back.eval(model.optimizer.lr)))

            for layer in model.layers:

                if "LSTM" in layer.name:
                    mlflow.log_param(f"model_{indx} - {layer.name} filters", str(layer.units))
                    mlflow.log_param(f"model_{indx} - {layer.name} kernel_initializer",
                                     str(layer.kernel_initializer.__class__.__name__))
                    mlflow.log_param(f"model_{indx} - {layer.name} recurrent_initializer",
                                     str(layer.recurrent_initializer.__class__.__name__))
                if "DropOut" in layer.name:
                    mlflow.log_param(f"model_{indx} - {layer.name} filters", str(layer.rate))
                if "Dense" in layer.name:
                    mlflow.log_param(f"model_{indx} - {layer.name} units", str(layer.units))

    def __track_general_params(self) -> None:
        mlflow.log_param("prediction_horizon", self.__config.forecasthorizon)
        mlflow.log_param("epochs", self.__config.lstmGparams.epochs)
        mlflow.log_param("batches", self.__config.lstmGparams.batches)
        mlflow.log_param("early_stopping", self.__config.lstmGparams.earlystopping)
        mlflow.log_param("lstm_activation", self.__config.lstmGparams.actfunc)
        mlflow.log_param("dense_stopping", self.__config.lstmGparams.densactfunc)
        mlflow.log_param("classification_activation", self.__config.lstmGparams.classactfunc)
        mlflow.log_param("datetime", self.__unique_id)

    def __track_extra_info(self) -> None:
        tracking_info = self.__tracking_info
        for item in tracking_info:
            mlflow.log_param(item, tracking_info[item])

    def __track_classification_metrics(self) -> None:
        for element in self.__prediction_metrics:
            mlflow.log_metric(f"{element}", self.__prediction_metrics[element])

    def __create_experiment_name(self) -> str:
        return self.__config.modelname.modelname + "_" + self.__unique_id

    def execute_tracking(self) -> None:

        mlflow.set_experiment(experiment_name=self.__create_experiment_name())
        with mlflow.start_run(run_name=f"run_{self.__create_experiment_name()}") as run:
            self.__track_hyper_params()
            print("HPs")
            self.__track_general_params()
            print("GPs")
            self.__track_extra_info()
            print("InfoTracker")
            self.__track_classification_metrics()
            print("METRICS")
