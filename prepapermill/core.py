import dataclasses
import pathlib
import sys
import typing

import click
import papermill as pm
import yaml


@click.command()
@click.argument('filenames', nargs=-1)
@click.option('--kernel-name', default=None, help='Name of kernel to run')
@click.option('--parameter-file', default='prepapermill.yaml', show_default=True)
def main(filenames, kernel_name, parameter_file):
    try:
        with open(parameter_file) as fin:
            settings = yaml.safe_load(fin)
    except Exception as exc:
        raise exc
    kwargs = {}
    kwargs['kernel_name'] = kernel_name
    for filename in filenames:
        filename = pathlib.Path(filename)
        if filename.suffix.endswith('.ipynb'):
            parameters = settings.get(filename.name, None)
            if parameters:
                nb = Notebook(filename=filename, parameters=parameters['parameters'], kwargs=kwargs)
                nb.execute()


@dataclasses.dataclass
class Notebook:
    filename: pathlib.Path
    parameters: typing.List[dict]
    kwargs: dict

    def __post_init__(self):
        self.filename = pathlib.Path(self.filename)
        self.stem = self.filename.stem
        self.output_dir = self.filename.parent.absolute() / 'output'
        self.output_dir.mkdir(parents=True, exist_ok=True)
        # TODO validate parameters

    def execute(self):
        for parameters in self.parameters:
            output_name = (
                self.stem + '_' + '_'.join(f'{key}_{value}' for key, value in parameters.items())
            )
            output_name += '.ipynb'
            output_path = self.output_dir / output_name
            pm.execute_notebook(
                self.filename.as_posix(),
                output_path.as_posix(),
                parameters=parameters,
                **self.kwargs,
            )
