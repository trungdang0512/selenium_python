class SoftAssert:
    errors = []

    @staticmethod
    def soft_assert(assertion_func, *args, **kwargs):
        message = kwargs.pop('message', None)
        try:
            assertion_func(*args, **kwargs)
        except AssertionError as e:
            if message is None:
                message = str(e)
            else:
                message = f"{message}: {str(e)}"
            SoftAssert.errors.append(message)

    @staticmethod
    def assert_all():
        if SoftAssert.errors:
            raise AssertionError(f"The list of FAILED soft assertions:\n" + "\n".join(SoftAssert.errors))

    @staticmethod
    def reset():
        SoftAssert.errors = []