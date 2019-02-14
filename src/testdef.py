# DEFINES: testing infrastructure using nested dicts

# GIVEN: dictionary of tests and test data
# Model 01
sample_tests_001 = {
    'alpha': {
        'criteria1': 'expected1',
        'criteria2': 'expected2',

    },
    'beta': {
        'criteria': 'expected'
    }
}

# Model 02
test_set_002 = {
    'function:foo': {
        'n_params': 'i_num',
        'param_a': 'a_val',
        # ...
        'param_i': 'i_val',
        'expected_result': 'e_val'
    },
    'function:bar': {
        'expected_result': 'e_val'
    }
}

# Model 03
dynamic_model_003 = {
    'function:foobar': {
        'n_params': 'i_num',                # may not be required, could use length params?
        'params': [0, 1, 2, 3],             # which may be stored as string or num? null means default value?
        'expected_result': 'e_val'
    }
}
# NOTE: instead of using dicts to encapsulate, consider storing a vector of used params


# EXECUTE: specified test function and compare to value stored in dict
# TODO: DEFINE method to run tests from dict
# def run_test_suite():
#    return

# FORMAT: RUN compare(alpha(criteria_i): return, expected_i) foreach i in N
# TODO: comparison testing foreach function defined in tests dict

# RETURN: if expected matches actual return success, record all results
# TODO: test logging functionality
