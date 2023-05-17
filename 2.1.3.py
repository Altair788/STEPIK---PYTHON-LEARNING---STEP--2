sentence = input()
cost_of_sentence = len(sentence) * 60
cost_in_rub = cost_of_sentence // 100
cost_in_pennies = cost_of_sentence % 100
print(cost_in_rub, 'р.', cost_in_pennies, 'коп.')
