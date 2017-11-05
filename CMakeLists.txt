cmake_minimum_required(VERSION 3.6)
project(hackfdu)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
find_package(OpenCV)
INCLUDE_DIRECTORIES(/home/guan/caffe/py-R-FCN/caffe/include /usr/local/cuda-8.0/targets/x86_64-linux/include
        /home/guan/caffe/py-R-FCN/caffe/.build_release/src/)
LINK_DIRECTORIES(/home/guan/caffe/py-R-FCN/caffe/build/lib)
set(SOURCE_FILES
    diaoyong.cpp)

add_executable(hackfdu ${SOURCE_FILES})