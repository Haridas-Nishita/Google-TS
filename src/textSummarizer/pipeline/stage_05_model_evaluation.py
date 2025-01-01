from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.conponents.model_evaluation import ModelEvaluation
from src.textSummarizer.logging import logger
from evaluate import load as load_metric
from datasets import load_dataset, load_from_disk



class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()