class DFA:
    def __init__(self, states, alphabet, transition, start, accept):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.start = start
        self.accept = accept
        
    def simulate(self, input_string):
        current_state = self.start
        for symbol in input_string:
            current_state = self.transition[current_state][symbol]
        return current_state in self.accept

states = {0, 1, 2, 3, 4}
alphabet = {'0', '1'}
transition = {
    0: {'0': 0, '1': 1},
    1: {'0': 2, '1': 3},
    2: {'0': 4, '1': 0},
    3: {'0': 1, '1': 2},
    4: {'0': 3, '1': 4}
}
start = 0
accept = {0}


dfa = DFA(states, alphabet, transition, start, accept)
x=input("Enter the binary number:")
print(f"{x} is a binary number divisible by 5:{dfa.simulate(x)}")