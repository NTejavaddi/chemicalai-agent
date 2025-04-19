from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
import numpy as np

def mock_get_yield_prediction(temperature, pressure, catalyst_conc, residence_time):
    yield_pred = 0.3 * np.log(temperature) + 0.5 * np.sqrt(pressure) - 2 * catalyst_conc + 0.2 * residence_time
    return {"predicted_yield": round(yield_pred, 2)}

def tool_predict_yield(params):
    t, p, c, r = map(float, params.split(","))
    return mock_get_yield_prediction(t, p, c, r)

llm = OpenAI(temperature=0.2)

tools = [
    Tool(
        name="PredictYield",
        func=tool_predict_yield,
        description="Input: temperature, pressure, catalyst_conc, residence_time"
    )
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
