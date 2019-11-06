#include <iostream>

using namespace std;

int main()
{
	int n, v[100], i, numar_unic = 0;
	cout << "n = ";
	cin >> n;

	if (n < 0)
		return -1;

	for (i = 0; i < n; i++) {
		cout << "v[" << i << "] = ";
		cin >> v[i];
	}

	for (i = 0; i < n; i++)
		numar_unic ^= v[i];

	if (numar_unic == 0)
		cout << "No unique number in array";
	else
		cout << "The unique number in array is " << numar_unic;

	return 0;
}
