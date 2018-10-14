from flask_migrate import MigrateCommand
from flask_script import Manager

from App import createApp


ab = createApp()

manager = Manager(ab)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
