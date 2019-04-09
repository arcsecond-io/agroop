import click

from . import __version__
from .options import State, basic_options

pass_state = click.make_pass_decorator(State, ensure=True)

VERSION_HELP_STRING = "Show the CLI version and exit."
BAD_PARAMETER_STRING = "(empty)"

def get_input(ctx, param, value):
    if not value and not click.get_text_stream('stdin').isatty():
        return click.get_text_stream('stdin').read().strip()
    else:
        return value


@click.command(short_help="Input coordinates list (JSON, XML or simple lines)")
@click.option('-V', is_flag=True, help=VERSION_HELP_STRING)
@click.option('--version', is_flag=True, help=VERSION_HELP_STRING)
@click.option('-h', is_flag=True, help="Show this message and exit.")
@click.argument('ref', required=False)
@click.argument('dist', type=float, required=False)
@click.argument('input', callback=get_input, required=False)
@click.pass_context
def main(ctx, ref, dist, input, version=False, v=False, h=False):
    """Approximately filter input according to coordinates distance.

    agroop reads a coordinates list INPUT and filters out those that are at a distance DIST expressed in arcseconds
    (of course...) shorter or equal to a reference position REF.
    """

    # We handle version and help before anything else to be able to use "agroop -h" and get help,
    # which cannot be handled if we require all parameters (ref and dist) first (agroop -h will fail
    # saying REF is missing). Hence the required=False for ref and dist too, replaced by their handling
    # below. Same for INPUT, with the key difference INPUT is setup to also come from stdin.
    if version or v:
        click.echo(__version__)
        return
    elif h:
        click.echo(ctx.get_help())
        return

    if not ref:
        raise click.BadParameter(BAD_PARAMETER_STRING, ctx=ctx, param_hint='REF')
    if not dist:
        raise click.BadParameter(BAD_PARAMETER_STRING, ctx=ctx, param_hint='DIST')

    # We must use required=False to handle stdin. But consequently,
    # we must handle the case where it is missing.
    if not input:
        raise click.BadParameter(BAD_PARAMETER_STRING, ctx=ctx, param_hint='INPUT')

    if ref and dist and input:
        click.echo(ref + '|' + str(dist) + '|' + input)
