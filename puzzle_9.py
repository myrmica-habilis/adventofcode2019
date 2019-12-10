from intcode_computer import execute_program

if __name__ == '__main__':
    with open('puzzle_9_input') as f:
        memory = tuple(int(elem) for elem in f.read().split(','))

    # Part 1
    outputs = list(execute_program([list(memory), 0], [1]))
    print(f'Solution: {outputs[0]}')

    # Part 2
    outputs = list(execute_program([list(memory), 0], [2]))
    print(f'Solution: {outputs[0]}')