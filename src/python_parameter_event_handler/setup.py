from setuptools import find_packages, setup

package_name = 'python_parameter_event_handler'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kaspar',
    maintainer_email='kaspar@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_with_parameters = python_parameter_event_handler.parameter_event_handler:main',
        ],
    },
)
