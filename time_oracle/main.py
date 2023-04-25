import typer
import random


def ask_input():
    month = int(typer.prompt("What is the current month?(1-12)"))
    year = int(typer.prompt("What is the current year?"))
    return month, year


def generate_time(month, year):
    random.seed(month * year)
    return random.randint(5, 15)


def check_input(month, year):
    msg = ""
    invalid = False
    if month < 1 or month > 12:
        msg += "Invalid month. Please enter a number between 1 and 12 "
        invalid = True
    if year < 2023 or year > 2050:
        msg += "Invalid year. Please enter a number between 2023 and 2050"
        invalid = True
    if invalid:
        typer.echo(msg)
        return False
    else:
        return True


def main():
    month, year = ask_input()
    if check_input(month, year):
        typer.echo(generate_time(month, year))
    else:
        main()


if __name__ == "__main__":
    typer.run(main)
