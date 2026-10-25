import numpy as np

# Столбцы — три испытания
scores = np.array([
    [10, 15, 20],  # участник 1
    [12, 18, 16],  # участник 2
    [14, 10, 18],  # участник 3
    [20, 16, 12]   # участник 4
])

# Прибавки за испытания: первое, второе, третье
trial_bonus = np.array([1, 2, 3])

# Личная прибавка каждого участника ко всем его результатам
person_bonus = np.array([
    [1],  # участник 1
    [2],  # участник 2
    [3],  # участник 3
    [4]   # участник 4
])
#5)Сохранить средние участников с keepdims=True, вычесть их из scores, проверить средние строк и формы массивов.
average2=np.mean(scores,axis=1,keepdims=True)
scores_centered=scores-average2
print(scores_centered)
print(average2.shape)                 # (4, 1)
print(scores_centered.shape)          # (4, 3)
print(np.mean(scores_centered, axis=1))
##############4)Вычислить средние по испытаниям, вычесть их из исходного scores,
#  сохранить в centered. Проверить средние столбцов — они должны быть близки к нулю############
average=np.mean(scores,axis=0)
centered=scores-average
print(np.mean(centered,axis=0))
##########################################################################
# 2)Прибавить trial_bonus к scores, сохранить в by_trial.
# 3)Прибавить person_bonus к scores, сохранить в by_person
by_trial=scores + trial_bonus
by_person=scores + person_bonus
print(by_trial)
print(by_person)
######################################################################################
##########1)Вывести формы трёх массивов и объяснить форму person_bonus#############
print(scores.shape)
print(trial_bonus.shape)
print(person_bonus.shape)
#персональный бонус прибавляется к каждому результату участника
#personal_bonus_scores один столбец и четыре строчки 
#################################################################################