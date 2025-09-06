from conan.tools import CppInfo
from conan.internal.util.files import save
import os

class KconfigDeps:
    def __init__(self, conanfile):
        self._conanfile = conanfile
        self._generator_file = 'Kconfig.conandeps'

    def generate(self):
        save(self._generator_file, self._content)


    @property
    def _content(self):
        s = 'menu "SiFli External Components"\n\n'
        for req, dep in self._conanfile.dependencies.items():
            libdir = os.path.normpath(dep.cpp_info.libdirs[0]).replace('\\', '/')
            s += f'orsource "{libdir}/Kconfig"\n'

        s += '\nendmenu\n'

        return s
