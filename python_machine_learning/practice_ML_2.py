import numpy as np
hours=np.array([1,2,3,4,5,6,7,8])
scores = np.array([10,20,30,40,50,60,70,80])
mean_value=np.mean(hours)
standard_deviation=np.std(hours).round(2)

scores=scores.astype(float)

scores_min=np.min(scores)
scores_max=np.max(scores)

if scores_min==scores_max:
  scores_norm=np.zeros_like(scores).round(2)
else:
  scores_norm = ((scores - scores_min) / (scores_max - scores_min)).round(2)


print(f"mean value:{mean_value}")
print(f"standard deviation:{standard_deviation}")
print(f"scores normalization :{scores_norm}")
