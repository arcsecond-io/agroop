import click


class State(object):
    def __init__(self, verbose=0, debug=False):
        self.verbose = verbose
        self.debug = debug

    def make_new_silent(self):
        return State(verbose=0, debug=self.debug)


def verbose_option_constructor(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        state.verbose = value
        return value

    return click.option('-v',
                        '--verbose',
                        count=True,
                        expose_value=False,
                        help='Increases verbosity.',
                        callback=callback)(f)


def debug_option_constructor(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        state.debug = value
        return value

    return click.option('-d',
                        '--debug',
                        is_flag=True,
                        expose_value=False,
                        help='Enables or disables debug mode (for arcsecond developers).',
                        callback=callback)(f)


def basic_options(f):
    f = verbose_option_constructor(f)
    f = debug_option_constructor(f)
    return f
