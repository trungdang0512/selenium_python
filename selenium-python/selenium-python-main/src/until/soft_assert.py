class SoftAssert:
    errors = []

    @staticmethod
    def soft_assert(assertion_func, message=None):
        try:
            assertion_func()
        except AssertionError as e:
            if message is None:
                message = "Assertion failed"
            SoftAssert.errors.append(message)


    @staticmethod
    def assert_all():
        if SoftAssert.errors:
            raise AssertionError(f"Các soft assertion thất bại:\n" + "\n".join(SoftAssert.errors))