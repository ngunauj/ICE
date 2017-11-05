#include "caffe/caffe.hpp"
#include <caffe/caffe.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <algorithm>
#include <iosfwd>
#include <memory>
#include <string>
#include <utility>
#include <vector>
using namespace caffe;
int main() {
    cv::Mat img_resized;
    cv::Mat img = cv::imread("1.jpg");
    cv::resize(img, img_resized, cv::Size(28, 28));

    boost::shared_ptr< Net<float> > net(new caffe::Net<float>("lenet.prototxt", TEST));

    net->CopyTrainedLayersFrom("lenet_iter_10000.caffemodel");

    
    return 0;
}
