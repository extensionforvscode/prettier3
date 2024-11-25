
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <omp.h>

using namespace std;

class QuickSortMultiThreading {
public:
	QuickSortMultiThreading(int start, int end, vector<int>& arr) 
		: start_(start), end_(end), arr_(arr) {}
	
	
	int partition(int start, int end, vector<int>& arr) {
		int i = start;
		int j = end;

		int pivoted = rand() % (j - i + 1) + i;

		
		int t = arr[j];
		arr[j] = arr[pivoted];
		arr[pivoted] = t;
		j--;

		while (i <= j) {
			if (arr[i] <= arr[end]) {
				i++;
				continue;
			}
			if (arr[j] >= arr[end]) {
				j--;
				continue;
			}
			t = arr[j];
			arr[j] = arr[i];
			arr[i] = t;
			j--;
			i++;
		}

		
		t = arr[j + 1];
		arr[j + 1] = arr[end];
		arr[end] = t;
		return j + 1;
	}

	
	void operator() () {
		// Base case
		if (start_ >= end_) {
			return;
		}

		int p = partition(start_, end_, arr_);

		QuickSortMultiThreading left(start_, p - 1, arr_);
		QuickSortMultiThreading right(p + 1, end_, arr_);

		#pragma omp parallel sections
		{
			#pragma omp section
			{
				left();
			}
			#pragma omp section
			{
				right();
			}
		}
	}

private:
	int start_;
	int end_;
	vector<int>& arr_;
};

int main() {
	int n = 7;
	vector<int> arr = {54, 64, 95, 82, 12, 32, 63};
	srand(time(NULL));
	QuickSortMultiThreading(0, n - 1, arr)();
	for (int i = 0; i < n; i++) {

		// Print sorted elements
		cout << arr[i] << " ";
	}
	cout << endl;
	return 0;
}
