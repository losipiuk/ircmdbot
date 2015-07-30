from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


# Inspired by the example at https://pytest.org/latest/goodpractises.html
class NoseTestCommand(TestCommand):
    user_options = [('nose-args=', 'a', "Arguments to pass to nose")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.nose_args = ''

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Run nose ensuring that argv simulates running nosetests directly
        import nose

        nose.run_exit(argv=['nosetests'] + self.nose_args.split(','))


requirements = [
    'irc==12.4.3',
    'PyYAML==3.11'
]

test_requirements = [
]

setup_requirements = [
    'flake8'
]

setup(
    name='ircmdbot',
    version='0.1',
    description='Simple IRC bot for running aliased shell commands',
    author='Lukasz Osipiuk',
    author_email='lukasz@osipiuk.net',
    keywords='irc bot shell remote command',
    url='https://github.com/losipiuk/ircmdbot',
    packages=find_packages(exclude=['*tests*']),
    package_dir={'ircmdbot': 'ircmdbot'},
    test_suite='test',
    install_requires=requirements,
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    entry_points={'console_scripts': ['ircmdbot = ircmdbot.main:main']},
    cmdclass={'test': NoseTestCommand}
)
