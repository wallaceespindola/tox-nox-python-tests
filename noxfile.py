import nox

# Have in mind that the Python versions listed here must be installed in the machine to run all target version tests
@nox.session(python=["3.8", "3.9", "3.10", "3.11", "3.12", "3.13"])
def tests(session):
    session.install("poetry")
    session.run("poetry", "install", "--no-interaction", "--no-root")
    session.run("pytest")