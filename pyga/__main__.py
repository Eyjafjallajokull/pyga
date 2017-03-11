from .cli import cli


_CLI_NAME = 'pyga'


def main(args=None):
    cli(prog_name=_CLI_NAME)


if __name__ == "__main__":
    main()
