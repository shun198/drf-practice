import os


if os.environ.get("CI_MAKING_DOCS") is not None:
    from pytest_bdd import scenarios

    scenarios(
        "features/health_check.feature",
        "features/login.feature",
    )
