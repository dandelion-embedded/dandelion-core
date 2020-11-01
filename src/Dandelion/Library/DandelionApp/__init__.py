import ujson


class AppVersion:
    def __init__(self, dt):
        self.schema = dt['schema']
        if self.schema == 1:
            self.fromv1dict(dt)

    def fromv1dict(self, dt):
        self.major = dt['major']
        self.minor = dt['minor']
        self.revision = dt['revision']


class DandelionAppManifest:

    def __init__(self, j, path):

        # Set module name
        self.moduleName = path

        # Load JSON and select correct decoder
        jsondict = ujson.load(j)
        self.schema = jsondict['schema']
        if self.schema == 1:
            self.fromv1dict(jsondict['application'])

    def fromv1dict(self, dt):
        self.name = dt['name']
        self.developer = dt['developer']
        self.version = AppVersion(dt['version'])
        self.systemApp = dt['systemApp']
        self.launcher = dt['launcher']
        self.visibleInLauncher = dt['visibleInLauncher']
        self.iconPath = dt['iconPath']
