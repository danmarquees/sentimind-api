# app/schemas.py

from pydantic import BaseModel, Field


# Schema para o corpo da requisição de análise
class AnalysisRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=3,
        description="Texto a ser analisado. Deve ter no mínimo 3 caracteres.",
    )


# Schema para a resposta da análise de sentimento
class SentimentResponse(BaseModel):
    label: str = Field(
        ..., description="O rótulo do sentimento (e.g., 'positivo', 'negativo')."
    )
    score: float = Field(..., description="A pontuação de confiança do modelo (0 a 1).")
