extern "C"
{
  float sum_float_numpy_array(float* a, int n);
  float biggest_abs_eigenvalue(float* A, int n); // biggest eigenvalue of square (n x n) matrix A
}


#include <Eigen/Core>
#include <Eigen/Eigenvalues>
using namespace Eigen;


float sum_float_numpy_array(float* a, int n)
{
  Map<VectorXf> bubi(a, n);
  return bubi.sum();
}


float biggest_abs_eigenvalue(float*  A, int n)
{
  Map<MatrixXf> m(A, n, n);
  return m.eigenvalues().cwiseAbs().array().maxCoeff();
}
