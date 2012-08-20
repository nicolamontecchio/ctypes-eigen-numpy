extern "C" 
{
	float sum_float_numpy_array(float* a, int n);
}


#include <Eigen/Core>
using namespace Eigen;


float sum_float_numpy_array(float* a, int n)
{
	Map<VectorXf> bubi(a, n);
	return bubi.sum();
}
