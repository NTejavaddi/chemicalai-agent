def mock_model_predict(temperature, pressure, catalyst_conc, residence_time):
    import numpy as np
    return 0.3 * np.log(temperature) + 0.5 * np.sqrt(pressure) - 2 * catalyst_conc + 0.2 * residence_time

class InputData:
    def __init__(self, temperature, pressure, catalyst_conc, residence_time):
        self.temperature = temperature
        self.pressure = pressure
        self.catalyst_conc = catalyst_conc
        self.residence_time = residence_time

def predict(data):
    y_pred = mock_model_predict(data.temperature, data.pressure, data.catalyst_conc, data.residence_time)
    return {"predicted_yield": round(y_pred, 2)}
