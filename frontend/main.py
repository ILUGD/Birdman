"""Frontend CLI for Birdman"""

import click

click.clear()

@click.command()
def details():

    """Function to input details from the user."""

    venue_decided = click.confirm("Venue Decided")
    _venue = None
    _date = None
    _time = None

    if venue_decided:

        meetup_link = click.prompt("Meetup Link", type=click.STRING)
        poster_link = click.prompt("Poster Link", type=click.STRING)
        tg_usrname = click.prompt("Telegram Username", type=click.STRING)
        talk_decided = click.confirm("Talks Decided")

        if talk_decided:
            write_file(meetup_link, poster_link, _date, _time, _venue)

            click.secho("Processing...(saving to "
                        f".birdman/<{_date}>/meetup.txt)\n", fg="green")

            click.secho("Contents of 'meetup.txt' file.\n", fg="yellow")

            with open("meetup.txt", "r") as fout:
                click.echo(fout.read())

            choice = click.confirm("Would you like to edit this?")

            if choice:
                click.edit(filename="meetup.txt", require_save=True)

            else:
                click.secho("Details written in meetup.txt", fg="blue")

        else:
            click.secho("Open Call for Proposals.\n", fg="red")
            click.secho("Open issues on Github.\n", fg="red")

    else:
        click.confirm("Ask for admin approval")
        click.echo("Send emails to POCs (Person of Contacts).")

def write_file(meetup_link, poster_link, _date, _time, _venue):

    """Function created to write details on the file."""

    with open("meetup.txt", "w+") as file:
        file.write(f"Meetup Link: {meetup_link}\n")
        file.write(f"Poster Link: {poster_link}\n")
        file.write("Join us for the next ILUG-D meetup "
                   f"at <{_date}/{_time}> at <{_venue}>\n")
