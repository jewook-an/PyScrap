import pandas as pd

class PandasHandler:
    @staticmethod
    def save_to_csv(data, filepath):
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)

    @staticmethod
    def load_from_csv(filepath):
        return pd.read_csv(filepath)