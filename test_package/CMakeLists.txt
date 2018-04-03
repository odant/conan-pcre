project(PackageTest C)
cmake_minimum_required(VERSION 3.0)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

enable_testing()

add_executable(test_pcre_CONAN_PKG test_pcre.c)
target_link_libraries(test_pcre_CONAN_PKG CONAN_PKG::pcre)
set_target_properties(test_pcre_CONAN_PKG
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_pcre_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/bin
    COMMAND test_pcre_CONAN_PKG
)

find_package(PCRE REQUIRED)
message(STATUS "PCRE_VERSION: ${PCRE_VERSION}")

add_executable(test_pcre test_pcre.c)
target_link_libraries(test_pcre PCRE::PCRE)
set_target_properties(test_pcre
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_pcre
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/bin
    COMMAND test_pcre
)
