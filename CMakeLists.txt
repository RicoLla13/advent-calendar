cmake_minimum_required(VERSION 3.10)
project(Advent-Calendar)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(utils STATIC utils.cpp utils.hpp)

file(GLOB SUBDIRECTORIES RELATIVE ${CMAKE_SOURCE_DIR} day_*)
foreach(SUBDIR ${SUBDIRECTORIES})
    if(IS_DIRECTORY ${CMAKE_SOURCE_DIR}/${SUBDIR})
        # Extract the name for the executable (same as subdirectory name)
        string(REPLACE "/" "_" EXEC_NAME ${SUBDIR})
        
        add_executable(${EXEC_NAME} ${SUBDIR}/main.cpp)
        target_link_libraries(${EXEC_NAME} PRIVATE utils)
    endif()
endforeach()
