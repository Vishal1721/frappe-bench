import click

@click.command()
def hello():
    print("Hello from the custom Bench CLI!")

commands = [hello]


# //asisgnment

@click.command("hello-app")
def hello_app():
    print("Hello from custom command!")

commands = [
    hello_app
]