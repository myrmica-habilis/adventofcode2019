from itertools import permutations, cycle

from intcode_computer import execute_program


def get_output_signal(memory, phases):
    value = 0
    for phase in phases:
        value = next(execute_program(memory.copy(), [phase, value]))
    return value


def run_feedback_loop(memory, phases):
    memories = [memory.copy() for __ in range(5)]
    input_buffers = [[] for __ in range(5)]
    amplifiers = []
    value = 0
    init_phase = True

    for amp in cycle(range(5)):
        if init_phase:
            input_buffers[amp].extend([phases[amp], value])
            amplifiers.append(execute_program(memories[amp], input_buffers[amp]))
        else:
            input_buffers[amp].append(value)

        if amp == 4:
            init_phase = False

        try:
            value = next(amplifiers[amp])
        except StopIteration:
            return value


if __name__ == '__main__':
    with open('puzzle_7_input') as f:
        memory = [int(elem) for elem in f.read().split(',')]

    # Part 1
    solution = max(get_output_signal(memory, phases)
                   for phases in permutations(range(5), 5))
    print(f'Solution: {solution}')

    # Part 2
    solution = max(run_feedback_loop(memory, phases)
                   for phases in permutations(range(5, 10), 5))
    print(f'Solution: {solution}')
