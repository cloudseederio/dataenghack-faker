from projen.python import PythonProject

project = PythonProject(
    author_email="phanssens1@gmail.com",
    author_name="Peter Hanssens",
    module_name="dataenghack_faker",
    name="dataenghack-faker",
    version="0.1.0",
    deps=[
        'faker'
    ]
)

project.synth()