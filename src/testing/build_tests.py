import logger
from constants import LogNames
from testing import arena_tests, model_tests

log = logger.log(LogNames.BUILD.value, console_logging=True, level=logger.INFO)

log.info('Starting arena tests')

arena_tests.run_test_arena()

log.info('Starting model tests')

model_tests.test_model_serialization()
