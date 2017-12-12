cmake_minimum_required(VERSION 2.8.12)

project(cmake_wrapper)

message(WARNING "Conan MySQL Connector/C Wrapped CMake")

include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")

# Instead the full conan_basic_setup, just these, so avoid messing with the output paths.
conan_check_compiler()
conan_flags_setup()

include("CMakeListsOriginal.cmake")

# -Werror causes build error with GCC 6.3/x86.
string(REPLACE " -Werror" "" CMAKE_C_FLAGS "${CMAKE_C_FLAGS}")
string(REPLACE " -Werror" "" CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
