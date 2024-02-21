import argparse
import random
from collections import abc
from pathlib import Path


def should_fail(fail_chance: float) -> bool:
    """
    Determine if the CI pipeline should fail.

    Values greater than or equal to `1` obviously automatically fail. I wish I could make them fail
    harder but we only have two outcomes unless we've entered the quantum realm.

    Negative values result in a `50%` failure chance as punishment for being cheeky.
    """
    if fail_chance >= 1:
        return True
    elif fail_chance == 0:
        # I don't care about floating point inaccuracies
        return False

    if fail_chance < 0:
        fail_chance = 0.5

    fate_of_the_universe = random.random()
    if fate_of_the_universe <= fail_chance:
        return True
    else:
        return False


def main(argv: abc.Sequence[str] | None = None) -> None:  # noqa: D103
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", type=Path)
    parser.add_argument("--fail-chance", type=float, default=0.05)
    args = parser.parse_args(argv)

    if should_fail(args.fail_chance):
        raise RuntimeError("Today is not your lucky day.")


if __name__ == "__main__":
    main()
