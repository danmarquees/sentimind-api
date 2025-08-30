from fastapi.testclient import TestClient
from app.main import app

# Criamos um cliente de teste que pode fazer requisições à nossa API em memória
client = TestClient(app)


def test_read_root():
    """Testa o endpoint raiz ("/") para garantir que a API está no ar."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API está no ar!"}


def test_analyze_positive_sentiment():
    """Testa o endpoint /analyze com um texto positivo."""
    response = client.post(
        "/analyze",
        json={"text": "Este é um dia maravilhoso e eu estou muito contente."},
    )
    json_data = response.json()

    assert response.status_code == 200
    assert "label" in json_data
    assert "score" in json_data
    assert "positivo" in json_data["label"]


def test_analyze_negative_sentiment():
    """Testa o endpoint /analyze com um texto negativo."""
    response = client.post(
        "/analyze", json={"text": "Que serviço horrível, estou muito desapontado."}
    )
    json_data = response.json()

    assert response.status_code == 200
    assert "negativo" in json_data["label"]


def test_analyze_invalid_input_too_short():
    """Testa o endpoint /analyze com um input inválido (texto muito curto)."""
    # O schema Pydantic define um `min_length=3`
    response = client.post("/analyze", json={"text": "oi"})

    # Um input inválido deve retornar um erro 422 Unprocessable Entity
    assert response.status_code == 422


def test_analyze_invalid_input_missing_field():
    """Testa o endpoint /analyze com um input inválido (campo 'text' faltando)."""
    response = client.post("/analyze", json={"message": "Isso está errado"})
    assert response.status_code == 422
