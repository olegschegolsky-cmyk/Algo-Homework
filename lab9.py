def get_next_state(needle: str, m: int, state: int, char: str) -> int:
    if state < m and char == needle[state]:
        return state + 1

    for next_state in range(state, 0, -1):
        if needle[next_state - 1] == char:
            is_suffix = True
            for i in range(next_state - 1):
                if needle[i] != needle[state - next_state + 1 + i]:
                    is_suffix = False
                    break
            if is_suffix:
                return next_state

    return 0


def find_substring(haystack: str, needle: str) -> list:
    if not needle:
        return []

    m = len(needle)
    n = len(haystack)
    alphabet = set(needle)

    transition_table = []
    for state in range(m + 1):
        state_transitions = {}
        for char in alphabet:
            state_transitions[char] = get_next_state(needle, m, state, char)
        transition_table.append(state_transitions)

    state = 0
    result = []

    for i in range(n):
        char = haystack[i]

        if char in alphabet:
            state = transition_table[state][char]
        else:
            state = 0

        if state == m:
            start_index = i - m + 1
            result.append(start_index)

    return result