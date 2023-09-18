import pandas as pd


class CrawlOutput:
    def __init__(self):
        self.dataFrame = None
        self.TextData = ''

    def SetDataFrame(self, dp: pd.DataFrame):
        self.dataFrame = dp
