import nox

nox.options.default_venv_backend = "uv"
nox.options.sessions = ["lint", "type_check"]


@nox.session
def lint(session: nox.Session) -> None:
    """Check for lint issues and proper formatting."""
    session.run_install(
        "uv",
        "sync",
        "--locked",
        "--quiet",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run("ruff", "check", "--no-fix")
    session.run("ruff", "format", "--check")


@nox.session
def tidy(session: nox.Session) -> None:
    """Fix any fixable lint issues and format the code."""
    session.run_install(
        "uv",
        "sync",
        "--locked",
        "--quiet",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run("ruff", "check", "--fix")
    session.run("ruff", "format")


@nox.session
def type_check(session: nox.Session) -> None:
    """Validate type correctness."""
    session.run_install(
        "uv",
        "sync",
        "--locked",
        "--quiet",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run("pyright")
