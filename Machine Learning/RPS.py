# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    else:
        opponent_history.clear()
      
    counter = {'R':'P','P':'S','S':'R'}
    guess = 'R'

    if len(opponent_history) >= 2:
        play_order = [''.join(opponent_history[k:k+4]) for k, v in enumerate(opponent_history[:-3])]
      
        to_play = [''.join([*opponent_history[-3:], v]) for v in ['S', 'R', 'P']]
      
        order = {k: play_order.count(k) for k in to_play}
      
        prediction = max(order, key=order.get)[-1]

        guess = counter[prediction]

    return guess