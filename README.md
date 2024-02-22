# pre-commit-fail-randomly
[![GitHub - License](https://img.shields.io/github/license/sco1/pre-commit-fail-randomly)](https://github.com/sco1/pre-commit-fail-randomly/blob/master/LICENSE)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sco1/pre-commit-fail-randomly/main.svg)](https://results.pre-commit.ci/latest/github/sco1/pre-commit-fail-randomly/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

Randomly fail a pre-commit run

## Using pre-commit-fail-randomly with pre-commit
Add this to your `.pre-commit-config.yaml`

```yaml
repos:
-   repo: https://github.com/sco1/pre-commit-fail-randomly
    rev: v0.1.0
    hooks:
    -   id: fail-randomly
        args: [--fail-chance=0.05]
```

## Hooks
### `fail-randomly`
Randomly fail your pre-commit pipeline. `fail-chance` may be optionally specified to change your failure chance (default: `0.05`). Ideally this is a float between `0` and `1`, inclusive, but you can do what you'd like and live with the consequences. If you specify a negative value then the universe has decided you get a 50/50 shot at failure.
