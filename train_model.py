import pickle
from model import OceanModel

exchange = "binance"
pair = "btc-usdt"
timeframe = "5m"


model = OceanModel(exchange, pair, timeframe)
model.train_from_csv(f"data/{exchange}_{pair}_{timeframe}_candles.csv")
model.pickle_model("./trained_models/")