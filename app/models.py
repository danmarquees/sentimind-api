# app/models.py

from transformers import pipeline
from functools import lru_cache

# Usamos um class para organizar a lógica relacionada ao modelo
class SentimentModel:
    def __init__(self):
        # O modelo é carregado apenas uma vez quando a classe é instanciada.
        # "lru_cache" ajuda a garantir que o pipeline seja criado apenas uma vez.
        self.pipeline = self._load_model()

    @lru_cache(maxsize=1)
    def _load_model(self):
        """Carrega o pipeline de análise de sentimento."""
        # Este modelo é multilíngue e bom para começar.
        # Em um projeto real, poderíamos escolher um modelo otimizado para português.
        model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
        print(f"Carregando o modelo: {model_name}...")
        sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)
        print("Modelo carregado com sucesso!")
        return sentiment_pipeline

    def analyze(self, text: str) -> dict:
        """
        Executa a análise de sentimento no texto fornecido.

        O modelo 'nlptown' retorna rótulos como '1 star', '5 stars'.
        Vamos mapeá-los para um formato mais amigável.
        """
        result = self.pipeline(text)[0]

        # Mapeamento de estrelas para rótulos de sentimento
        label_map = {
            '1 star': 'muito negativo',
            '2 stars': 'negativo',
            '3 stars': 'neutro',
            '4 stars': 'positivo',
            '5 stars': 'muito positivo'
        }

        # Retorna o resultado no formato que nossa API espera
        return {
            "label": label_map.get(result['label'], 'desconhecido'),
            "score": result['score']
        }

# Instanciamos o modelo aqui para que ele seja um "singleton"
# e seja carregado na inicialização do módulo.
sentiment_model = SentimentModel()

# Função auxiliar para ser usada na API, garantindo que o modelo seja injetado.
def get_sentiment_model():
    return sentiment_model
