class SoftAssert:
    errors = []

    @staticmethod
    def soft_assert(assertion_func, message=None):
        try:
            lambda: assertion_func()
        except AssertionError as e:
            if message is None:
                message = "Assertion failed"
            SoftAssert.errors.append(message)


    @staticmethod
    def assert_all():
        if SoftAssert.errors:
            raise AssertionError(f"The list of FAILED soft assertions :\n" + "\n".join(SoftAssert.errors))