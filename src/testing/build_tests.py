from src import logger
from src.constants import LogNames
from src.testing import arena_tests, model_tests

log = logger.log(LogNames.BUILD)

log.info('Starting arena tests')

arena_tests.run_test_arena()

log.info('Starting model tests tests')

model_tests.test_model_serialization()
