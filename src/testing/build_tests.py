from src import logger
from src.constants import LogNames
from src.testing import arena_tests, model_tests

# # TODO: Fix
log = logger.log(LogNames.BUILD.value, console_logging=True)
# logger.listen_to_log(LogNames.ARENA.value, logger.console(LogNames.ARENA.value))

log.info('Starting arena tests')

arena_tests.run_test_arena()

log.info('Starting model tests tests')

model_tests.test_model_serialization()
