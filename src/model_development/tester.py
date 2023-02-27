import os
import numpy as np
import tensorflow as tf
from sklearn.metrics import precision_score, recall_score, f1_score, average_precision_score, confusion_matrix


class Tester:

    def __init__(
            self,
            config,
            unique_id,
            test_data,
            test_labels,
            trained_model
    ):
        self.__config = config
        self.__unique_id = unique_id
        self.__tuner_obj = trained_model
        self.__test_data = test_data
        self.__test_labels = test_labels
        self.best_models = self.__extract_best_models(self.__tuner_obj)
        self.__save_best_models()

    @staticmethod
    def __extract_best_models(trained_tuner):
        return trained_tuner.get_best_models(num_models=2)

    def __save_best_models(self) -> None:
        dir2save = os.path.join(
            *self.__config.dirs2make.best_models,
            self.__config.modelname.modelname + self.__unique_id
        )
        for i in range(len(self.best_models)):
            self.best_models[i].save(os.path.join(dir2save, f"best_model_{i + 1}.h5"))

    def __predict_with_top1_model(self, test_data):
        top1_model = self.best_models[0]
        prediction = top1_model.predict(test_data)
        return prediction

    def execute_testing(self):
        target = self.__test_labels
        print(target)
        prediction_matrix = self.__predict_with_top1_model(test_data=self.__test_data)
        print(prediction_matrix)
        single_array_pred = np.argmax(prediction_matrix, axis=1)
        conf_matrix = confusion_matrix(target, single_array_pred).ravel()
        metrics = {
            "precision": precision_score(target, single_array_pred, average="micro"),
            "avg_precision": average_precision_score(target, prediction_matrix[:, 1], average="micro"),
            "recall": recall_score(target, single_array_pred, average="micro"),
            "f1": f1_score(target, single_array_pred, average="micro"),
            "tn": conf_matrix[0],
            "fp": conf_matrix[1],
            "fn": conf_matrix[2],
            "tp": conf_matrix[3]
        }
        return metrics
