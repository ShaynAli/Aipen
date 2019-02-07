# DEFINES: testing infrastructure using nested dicts

# GIVEN: dictionary of tests and test data
sample_tests = {
    'alpha': {
        'criteria1': 'expected1',
        'criteria2': 'expected2',

    },
    'beta': {
        'criteria': 'expected'
    }
}

# EXECUTE: specified test function and compare to value stored in dict
# TODO: DEFINE method to run tests from dict
# def run_test_suite():
#    return

# FORMAT: RUN compare(alpha(criteria_i): return, expected_i) foreach i in N
# TODO: comparison testing foreach function defined in tests dict

# RETURN: if expected matches actual return success, record all results
# TODO: test logging functionality
