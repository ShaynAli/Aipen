from testing import arena_tests, model_tests

print('Starting build tests')

print('Starting arena tests')
arena_tests.run_test_arena()
print('Completed arena tests')

print('Starting model tests')
model_tests.test_model_serialization()
print('Completed model tests')

print('Completed build tests')
