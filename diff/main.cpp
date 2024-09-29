#include <opencv2/opencv.hpp>
#include <iostream>
#include <cmath>

cv::Mat read(char const *fn)
{
    cv::Mat org = cv::imread(fn);
    cv::Mat r;
    org.convertTo(r, CV_64FC3);
    return r;
}

int main(int argc, char const *argv[])
{
    if (argc < 3)
    {
        return 1;
    }
    cv::Mat a = read(argv[1]);
    cv::Mat b = read(argv[2]);
    cv::Mat d = a - b;
    cv::Mat d2 = d.mul(d);
    cv::Mat a1, a2;
    cv::Scalar r = cv::mean(d2);
    double sum = 0;
    for (int e = 0; e < 3; ++e)
    {
        sum += std::sqrt(r[e]);
    }
    std::cout << (sum / 3) << std::endl;
    return 0;
}
