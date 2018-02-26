from conans import ConanFile, CMake


class PcreConan(ConanFile):
    name = "pcre"
    version = "8.41"
    license = "PCRE2 License https://www.pcre.org/licence.txt"
    description = "PCRE2 is a library of functions to support regular expressions whose syntax and semantics are as close as possible to those of the Perl 5 language."
    url = "https://github.com/odant/conan-pcre"
    settings = {
        "os": ["Windows", "Linux"],
        "compiler": ["Visual Studio", "gcc"],
        "build_type": ["Debug", "Release"],
        "arch": ["x86_64", "x86"]
    }
    generators = "cmake"
    exports_sources = "pcre-8.41/*", "CMakeLists.txt", "FindPCRE.cmake"
    no_copy_source = True
    build_policy = "missing"

    def configure(self):
        # Pure C library
        del self.settings.compiler.libcxx

    def build(self):
        cmake = CMake(self)
        #
        if self.settings.os != "Windows":
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE:BOOL"] = "ON"
        cmake.definitions["BUILD_SHARED_LIBS:BOOL"] = "OFF"
        #
        cmake.definitions["PCRE_BUILD_PCRE8:BOOL"] = "ON"
        cmake.definitions["PCRE_BUILD_PCRE16:BOOL"] = "OFF"
        cmake.definitions["PCRE_BUILD_PCRE32:BOOL"] = "OFF"
        cmake.definitions["PCRE_BUILD_PCRECPP:BOOL"] = "OFF"
        cmake.definitions["PCRE_EBCDIC:BOOL"] = "OFF"
        cmake.definitions["PCRE_EBCDIC_NL25:BOOL"] = "OFF"
        cmake.definitions["PCRE_BUILD_PCREGREP:BOOL"] = "OFF"
        cmake.definitions["PCRE_BUILD_TESTS:BOOL"] = "OFF"
        cmake.definitions["PCRE_SUPPORT_LIBZ:BOOL"] = "OFF"
        cmake.definitions["PCRE_SUPPORT_LIBBZ2:BOOL"] = "OFF"
        cmake.definitions["PCRE_SUPPORT_LIBEDIT:BOOL"] = "OFF"
        cmake.definitions["PCRE_SUPPORT_LIBREADLINE:BOOL"] = "OFF"
        if self.settings.os == "Windows" and self.settings.compiler == "Visual Studio":
            cmake.definitions["PCRE_STATIC_RUNTIME:BOOL"] = "OFF"
        #
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("FindPCRE.cmake", src=".", dst=".")
        self.copy("*pcre.h", dst="include", keep_path=False)
        self.copy("*pcre.lib", dst="lib", keep_path=False)
        self.copy("*pcred.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        
    def package_info(self):
        self.cpp_info.libs = ["pcre"]
        if self.settings.os == "Windows" and self.settings.build_type == "Debug":
            self.cpp_info.libs = ["pcred"]
        if self.settings.os == "Windows":
            self.cpp_info.defines.append("PCRE_STATIC")
