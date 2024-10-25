from models.train_module import TrainModule
from utils import initialize_logging, load_config

config = load_config(config_path="./config/config.yaml")
initialize_logging(config_path="./config/logging_config.yaml", debug=False)
trainer = TrainModule(config)
trainer.pipeline()
trainer.test()
