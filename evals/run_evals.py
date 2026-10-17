import json

from langchain_openai import ChatOpenAI
import requests
from openai import AsyncOpenAI
from ragas import EvaluationDataset, evaluate
from ragas.llms import llm_factory, LangchainLLMWrapper
from ragas.metrics import ContextPrecision, Faithfulness

from app.config import settings

if settings.llm_provider == "Ollama":
    llm = ChatOpenAI(
        model=settings.model,
        base_url=settings.llm_url,
        api_key=settings.api_key or "ollama",
    )
else:
    llm = ChatOpenAI(model=settings.model)

with open("evals/eval_dataset.json") as f:
    data = json.load(f)

eval_samples = []

for sample in data["samples"]:
    api_response = requests.post(
        "http://localhost:8000/api/v1/query", json={"prompt": sample["user_input"]}
    ).json()

    eval_samples.append(
        {
            "user_input": sample["user_input"],
            "response": api_response["answer"],
            "retrieved_contexts": api_response["contexts"],
            "reference": sample["reference"],
        }
    )

dataset = EvaluationDataset.from_list(eval_samples)
llm = LangchainLLMWrapper(llm)

results = evaluate(
    dataset=dataset,
    metrics=[Faithfulness(llm=llm), ContextPrecision(llm=llm)],
)

print(results)
