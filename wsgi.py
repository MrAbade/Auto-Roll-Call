from auto_rollcall import create_app

application = create_app()


@application.shell_context_processor
def make_shell_context():
    return dict(db=application.db)


if __name__ == "__main__":
    application.run("0.0.0.0")
