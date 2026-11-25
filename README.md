# Funniest One-Line Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/chiidaichii1-boop/hamsyh-out-of-office/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/chiidaichii1-boop/hamsyh-out-of-office/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

Entry for the make.fun bounty "Funniest One-Line Out-of-Office Reply":
https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8

## What it does

`main.py` (Python 3 standard library only, no network) writes a single
one-line out-of-office auto-reply to `entry.txt` in the output directory
named by the `MAKEFUN_OUTPUT_DIR` environment variable (default
`/output`). The output is deterministic: the same line, byte for byte,
on every run.

## The line

> I'm out of office; my inbox is now in the care of Future Me, a very
> confident intern with no password and no plan.

## Run it

```sh
python3 main.py
# writes entry.txt into /output (or $MAKEFUN_OUTPUT_DIR)
```

## License

MIT — see [LICENSE](LICENSE).
