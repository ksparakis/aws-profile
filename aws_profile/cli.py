# Copyright 2023 Konstantinos Sparakis
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import click
import os
import re
import pyperclip
from . import __version__
from simple_term_menu import TerminalMenu


@click.command()
@click.version_option(version=__version__, message='%(version)s')
def cli():
    profiles = get_profiles()
    selected = TerminalMenu(profiles, title="Select Your Profile", preview_size=0.75).show()
    set_aws_profile(profiles[selected])


def get_profiles():
    home_directory = os.path.expanduser('~')
    aws_config_file = open(f"{home_directory}/.aws/config", "r")
    aws_config = aws_config_file.read()
    regex = '\[profile.*\]'
    uncleaned_profiles = re.findall(regex, aws_config)
    profiles = list()
    for profile in uncleaned_profiles:
        parts = profile[1:-1].split(' ')
        profiles.append(parts[1])
    return profiles


def set_aws_profile(profile):
    os.environ["AWS_PROFILE"] = profile
    expt = f"export AWS_PROFILE={profile}"
    click.echo(expt)
    pyperclip.copy(expt)

