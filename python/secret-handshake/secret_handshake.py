ACTIONS = ['wink', 'double blink', 'close your eyes', 'jump', 'reverse']
ACTIONS_VALUE = {action: 2**i for i, action in enumerate(ACTIONS)}

def handshake(code):
    handshakes = [action for action, val in ACTIONS_VALUE.items() if code & val]
    if 'reverse' in handshakes:
        handshakes.remove('reverse')
        handshakes = handshakes[::-1]
    return handshakes

def secret_code(actions):
    code = sum(ACTIONS_VALUE[action] for action in actions)
    if len(actions) > 1:
        if ACTIONS_VALUE[actions[0]] > ACTIONS_VALUE[actions[1]]:
            code += ACTIONS_VALUE['reverse']
    return code
