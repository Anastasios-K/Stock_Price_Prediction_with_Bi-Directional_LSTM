class InfoTracker:
    train_set_duplicates: list = None
    test_set_duplicates: list = None
    train_set_NaNs: list = None
    test_set_NaNs: list = None
    class_weights: dict = {0: None, 1: None}

