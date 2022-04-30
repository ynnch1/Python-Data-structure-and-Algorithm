from opcode import stack_effect


stack = []

stack.append('e')
stack.append('f')
stack.append('g')

print('initial stack')
print(stack)

print('\nElements popped from stack:')
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)