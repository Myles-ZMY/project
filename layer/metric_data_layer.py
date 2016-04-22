from data_layer import DataLayer
from database import CUHK03
from utils import CHECK

BATCH = 128

class MetricDataLayer(DataLayer):
    def check(self, bottom, top):
        CHECK.EQ(len(top), 2)
        pass

    def batch_advancer(self):
        data, label = self.db.gen_pair(BATCH)
        self.buffer = (data, label)

    def init(self):
        self.db = CUHK03()
        self.db.load()
        pass