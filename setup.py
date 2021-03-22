from distutils.core import setup

try:
    with open('README.md') as file:
            long_description = file.read()
except IOError:
    long_description = "Easy to use color library for Discord.PY"

setup(
    name='Discord Colors',
    version='9',
    license='Apache License v2',
    author='Florian Leitner',
    author_email='florian.leitner@gmail.com',
    url='https://github.com/DaEpicSwag/DiscordColorPY',
    description='A Small Library For Discord.py Color Embeds',
    long_description=long_description,
    py_modules=['Dcolors'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Windows',
        'Operating System :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
)
