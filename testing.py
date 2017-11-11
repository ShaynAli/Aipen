import evaluation as ev
import numpy as np
import test_models

z_mdl = test_models.ZeroModel()

ev.eval_ml_model(z_mdl, x_data=np.zeros((100, 3)), y_data=np.zeros((100, 1)), batch_size=5)

# print(z_mdl.name())