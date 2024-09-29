CXX = c++
CXXFLAGS = -I/opt/homebrew/Cellar/opencv/4.10.0_6/include/opencv4/
LDFLAGS = -L/opt/homebrew/Cellar/opencv/4.10.0_6/lib/
LDLIBS =  -lopencv_core -lopencv_highgui -lopencv_imgcodecs
CXXVERSION = -std=c++20

imdiff: main.cpp
	$(CXX) $< -o $@ $(CXXFLAGS) $(CXXVERSION) $(LDFLAGS) $(LDLIBS)

clean :
	rm imdiff
