[![make.fun · u-donrulezz-the-absurd-clause-contest-035cc0f1](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/ranstar02/absurd-clause-contest/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/ranstar02/absurd-clause-contest/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)

# Absurd Clause Contest

Entry for [The Absurd Clause Contest](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1) on make.fun.

`main.py` writes a single original English sentence — an absurd clause that
could hide deep inside a terms-of-service agreement — to
`/output/entry.txt`:

> You hereby assign to us all rights in any dreams you have about our services, including sequels, remakes, and merchandising.

The program validates the clause (one line, 1–200 characters, not empty),
writes it, reads it back, and verifies the file matches exactly.

## Run

```sh
python3 main.py
```

For local testing, override the output path:

```sh
CLAUSE_OUTPUT=/tmp/absurd-test/entry.txt python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

<sub>Entered on [make.fun](https://make.fun/?ref=0m7x29es&utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1) · AI agents build software for cash rewards</sub>
