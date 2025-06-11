![Python](https://www.python.org/static/community_logos/python-logo-generic.svg)

# Using Tox, Nox and CI/CD for Multiple Python Versions Validation Tests

![MIT License](https://img.shields.io/badge/License-MIT-pink)
![Python](https://img.shields.io/badge/Built_with-Python-blue)
![Tox](https://img.shields.io/badge/Built_with-Tox-yellow)
![Nox](https://img.shields.io/badge/Built_with-Nox-purple)
![GitLab CI/CD](https://img.shields.io/badge/Powered_by-GitLab-orange)
![GitHub Actions CI/CD](https://img.shields.io/badge/Powered_by-GitHubActions-teal)

This project demonstrates the integration of **Tox**, **Nox**, **Poetry**, **CI/CD** and **Pytest** to validate
Python projects across multiple Python versions. This is specially useful for shared libs projects
and multi-user environments projects.

## Features

- Example functions for addition and subtraction.
- Unit testing on tht with `pytest`.
- Dependency and environment management with `Poetry`.
- Multi-version Python application testing with `Tox`, `Nox` and `CI/CD` (Gitlab and GitHub Actions).

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/wallaceespindola/tox-nox-python-tests.git
cd tox-nox-python-tests
```

### Install Poetry

```bash
pip install poetry
```

### Install Dependencies (listed in pyproject.toml)

```bash
poetry install
```

### Run Unit Tests

```bash
poetry run pytest --verbose
```

### Run Tox

```bash
poetry run tox
```

Example output:

![tox_output.png](resources/tox_output.png)

### Run Nox

```bash
poetry run nox
```

Example output:

![nox_output.png](resources/nox_output.png)

### References

This project was created to showcase how to validate Python projects across multiple Python versions using
Tox, Nox and CI/CD for automated testing, with dependency and environment management powered by Poetry.
It includes unit tests written with Pytest.
Here are some helpful references to understand the tools used in this project:

- [Tox Documentation](https://tox.wiki/en/).
- [Nox Documentation](https://nox.thea.codes/en/stable/).
- [Poetry Documentation](https://python-poetry.org/docs/).
- [Pytest Documentation](https://docs.pytest.org/en/stable/).
- [GitLab CI/CD Documentation](https://docs.gitlab.com/).
- [GitHub Actions CI/CD Documentation](https://docs.github.com/en/actions).

### Related Articles

- Dev.to: Test Python Code Like a Pro with Tox, Nox and CI/CD
- Dzone: Automating Python Multi-Version Testing with Tox, Nox and CI/CD

## Author

- Wallace Espindola, Sr. Software Engineer / Java & Python Dev
- **LinkedIn:** [linkedin.com/in/wallaceespindola/](https://www.linkedin.com/in/wallaceespindola/)
- **GitHub:** [github.com/wallaceespindola](https://github.com/wallaceespindola)
- **E-mail:** [wallace.espindola@gmail.com](mailto:wallace.espindola@gmail.com)
- **Twitter:** [@wsespindola](https://twitter.com/wsespindola)
- **Gravatar:** [gravatar.com/wallacese](https://gravatar.com/wallacese)
- **Dev Community:** [dev.to/wallaceespindola](https://dev.to/wallaceespindola)
- **DZone Articles:** [DZone Profile](https://dzone.com/users/1254611/wallacese.html)
- **Pulse Articles:** [LinkedIn Articles](https://www.linkedin.com/in/wallaceespindola/recent-activity/articles/)
- **Website:** [W-Tech IT Solutions](https://www.wtechitsolutions.com/)
- **Presentation Slides:** [Speakerdeck](https://speakerdeck.com/wallacese)

## License

- This project is released under the MIT License.
- See the [LICENSE](LICENSE) file for details.
- Copyright © 2025 [Wallace Espindola](https://github.com/wallaceespindola/).
