import nox

nox.options.default_venv_backend = "uv"
nox.options.sessions = ["lint", "type_check"]


@nox.session(venv_backend="none")
def lint(session: nox.Session) -> None:
    """Check for lint issues and proper formatting."""
    session.run("ruff", "check", "--no-fix")
    session.run("ruff", "format", "--check")


@nox.session(venv_backend="none")
def tidy(session: nox.Session) -> None:
    """Fix any fixable lint issues and format the code."""
    session.run("ruff", "check", "--fix")
    session.run("ruff", "format")


@nox.session(venv_backend="none")
def type_check(session: nox.Session) -> None:
    """Validate type correctness."""
    session.run("pyright")
