from fastapi import FastAPI, Depends
from .schemas import AnalysisRequest, SentimentResponse
from .models import SentimentModel, get_sentiment_model

# Cria a instância da aplicação FastAPI
app = FastAPI(
    title="Sentimind API",
    description="Uma API para análise de sentimento e sumarização de texto.",
    version="0.1.0",
)

# Endpoint de "health check" para verificar se a API está no ar
@app.get("/", tags=["Status"])
def read_root():
    return {"status": "API está no ar!"}


# Endpoint principal para análise de sentimento
@app.post("/analyze", response_model=SentimentResponse, tags=["Análise"])
def analyze_sentiment(
    request: AnalysisRequest,
    model: SentimentModel = Depends(get_sentiment_model)
):
    """
    Recebe um texto e retorna a análise de sentimento.

    - **text**: O texto a ser analisado.
    """
    result = model.analyze(request.text)
    return SentimentResponse(**result)
