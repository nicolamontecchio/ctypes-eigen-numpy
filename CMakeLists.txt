cmake_minimum_required (VERSION 2.6)
project (eigentest)

set(CMAKE_BUILD_TYPE Release)

# python wrappers
add_library(eigentestpy SHARED a.cpp)


# install stuff
install(TARGETS eigentestpy
            RUNTIME DESTINATION bin
            LIBRARY DESTINATION lib
            ARCHIVE DESTINATION lib/static)
