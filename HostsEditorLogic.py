class HostsEditorLogic:
    def __init__(self, config_path):
        self.hosts_path = self.load_config(config_path)

    def load_config(self, config_path):
        with open(config_path, 'r') as f:
            for line in f:
                key, value = line.strip().split('=')
                if key == 'hosts_file':
                    return value
        return ''

    def load_file(self):
        with open(self.hosts_path, 'r') as f:
            return f.read()

    def write_file(self, text):
        with open(self.hosts_path, 'w') as f:
            f.write(text)

    def restore_original(self):
        with open(self.hosts_path, 'r') as f:
            return f.read()
