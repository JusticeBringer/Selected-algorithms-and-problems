#include <iostream>
#include <stack>
#include <utility>
#include <algorithm>
#include <fstream>

using namespace std;

struct MyStruct
{
	int x = 0;
	int poz = 0;
};

int binary_search(stack <MyStruct> s[], int left, int right, int x) {
	int mid = left + (right - left) / 2;
	if (mid == right)
		return mid;

	if (right >= left) {
		if (s[mid].top().x == x)
			return mid;
		if (s[mid].top().x > x)
			return binary_search(s, mid + 1, right, x);
		if (s[mid].top().x < x)
			return mid;
		
	}
	return mid;
}

void afisare(stack <MyStruct> s[], int n, int nrRanduri) {
	ofstream fout("date.out");

	while(s[0].empty() == false) {
		int j = 0;
		cout << s[0].top().x << " ";
		fout << s[0].top().x << " ";

		for (j = 1; j < nrRanduri; j++)
			if (s[j].size() == s[0].size()) {
				cout << s[j].top().x << " ";
				fout << s[j].top().x << " ";

				s[j].pop();
			}
		
		s[0].pop();

		cout << "\n";
		fout << "\n";
	}
	fout.close();
}

void patience_sorting(stack <MyStruct> s[], int n, int nrRanduri, int sol[], int &count) {
	while (s[0].empty() == false) {
		int j = 0;
		sol[count++] = s[0].top().x;
		for (j = 1; j < nrRanduri; j++)
			if (s[j].size() == s[0].size()) {
				sol[count++] = s[j].top().x;
				s[j].pop();
			}

		s[0].pop();
	}
}

void show_patience(int sol[], int count) {
	for (int i = 0; i < count; i++)
		cout << sol[i] << " ";
}

int main()
{
	ifstream fin("date.in");
	ofstream fout("date.out");

	stack <MyStruct> s[100];
	
	int n, x;
	fin >> n;

	int copyN = n;

	if (n < 0) {
		fout << "Nu se poate - date incorecte";
		return 0;
	}
	if (n == 1) {
		fout << n;
		return 0;
	}

	fin >> x;
	s[0].push({ x, 0 });
	n--;

	int nrRanduri = 1;

	for (; n > 0; n--) {
		fin >> x;	

		if (x >= s[0].top().x)
			s[0].push({ x, 0 });
		else{
			int nou_poz = binary_search(s, 0, nrRanduri, x); //cautam binar
			s[nou_poz].push({ x, nou_poz });
			
			if(nou_poz == nrRanduri)
				nrRanduri++;
		}
	}

	int sol[1000], count = 0;

	//Pentru Patience sorting comentati linia urmatoare
	afisare(s, copyN, nrRanduri);

	patience_sorting(s, n, nrRanduri, sol, count);
	show_patience(sol, count);

	return 0;
}