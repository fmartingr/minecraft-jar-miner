import os
from fabric.api import task, local
from fabric.colors import yellow
from minecraft_pickaxe import config


@task
def unpack(version):
    """
    Unpacks and decompiles classes for the specified version
    """
    if not os.path.exists(os.path.join(config.VERSIONS_PATH, version)):
        raise Exception("Version {version} not found under {path}".format(
            version=version, path=config.VERSIONS_PATH
        ))

    path = os.path.join(config.VERSIONS_PATH, version)

    print(yellow('Version {}'.format(version)))

    # Unpack
    if not os.path.exists(os.path.join(path, 'jarfiles')):
        print(yellow('Unpacking...'))
        local('{cmd} {cmd_args}'.format(
            cmd=config.UNZIP,
            cmd_args=config.UNZIP_ARGS.format(
                jarfile='{}.jar'.format(os.path.join(path, version)),
                destination=os.path.join(path, 'jarfiles')
            )
        ))

    # Decompile
    if not os.path.exists(os.path.join(path, 'classes')):
        print(yellow('Decompiling...'))
        local(
            'ls {jarfiles}/*.class | xargs -n1 {cmd} {cmd_args} &> /dev/null'
            .format(
                jarfiles=os.path.join(path, 'jarfiles'),
                cmd=config.JAD,
                cmd_args=config.JAD_ARGS.format(
                    destination=os.path.join(path, 'classes')
                )
            ),
        )
        local('rm {}/*.class'.format(os.path.join(path, 'jarfiles')))


@task
def clean(version):
    """
    Cleans decompiled and unpacked files for the specified version.
    """
    if not os.path.exists(os.path.join(config.VERSIONS_PATH, version)):
        raise Exception("Version {version} not found under {path}".format(
            version=version, path=config.VERSIONS_PATH
        ))

    path = os.path.join(config.VERSIONS_PATH, version)

    local('rm -rf {path}/jarfiles {path}/classes'.format(path=path))


@task
def versions():
    """
    List all detected versions
    """
    versions = []
    contents = os.listdir(config.VERSIONS_PATH)
    for d in contents:
        if os.path.exists(os.path.join(
                config.VERSIONS_PATH, d, '{}.jar'.format(d))):
            versions.append(d)

    print(yellow('Versions detected:'))
    for version in versions:
        print(' - {}'.format(version))
