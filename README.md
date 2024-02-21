# pre-commit-fail-randomly
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

Randomly fail a pre-commit run

## Using pre-commit-fail-randomly with pre-commit
Add this to your `.pre-commit-config.yaml`

```yaml
repos:
-   repo: https://github.com/sco1/pre-commit-fail-randomly
    rev: v1.0.0
    hooks:
    -   id: fail-randomly
```

## Hooks
### `fail-randomly`
Randomly fail your pre-commit pipeline. `fail-chance` may be optionally specified to change your failure chance (default: `0.05`). Ideally this is a float between `0` and `1`, inclusive, but you can do what you'd like and live with the consequences. If you specify a negative value then the universe has decided you get a 50/50 shot at failure.
