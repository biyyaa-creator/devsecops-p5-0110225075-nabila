"""Application entry point."""
from app.commands import make_parser, run_command


def main() -> int:
    parser = make_parser()
    arguments = parser.parse_args()
    return run_command(arguments)


if __name__ == "__main__":
    raise SystemExit(main())
