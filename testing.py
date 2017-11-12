import evaluation as ev
import numpy as np
import test_models

z_mdl = test_models.ZeroModel()
r_mdl = test_models.RandomModel()

# mdls = [z_mdl, r_mdl]
mdls = [z_mdl, r_mdl]

scores = ev.score_ml_models(mdls, x_data=np.zeros((100, 3)), y_data=np.zeros((100, 1)))
print(scores)
