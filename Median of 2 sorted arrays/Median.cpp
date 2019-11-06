#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>

using namespace std;

float rezultat_final = 0;

void obtinere_mediana(vector <int> a, vector <int> b, int st_a, int st_b, int dr_a, int dr_b, int paritate_a, int paritate_b) {
	vector <int> c;
	c.resize(dr_a - st_a + dr_b - st_b + 2);
	int index_c = 0;

	for (; st_a <= dr_a && st_b <= dr_b;) {
		if (a[st_a] > b[st_b]) {
			c[index_c] = b[st_b];
			index_c++;
			st_b++;
		}
		else {
			c[index_c] = a[st_a];
			index_c++;
			st_a++;
		}
	}

	for (int i = st_a; i <= dr_a; i++) {
		c[index_c] = a[i];
		index_c++;
	}
	for (int i = st_b; i <= dr_b; i++) {
		c[index_c] = b[i];
		index_c++;
	}

	cout << "\nVectorul interclasat: ";
	for (auto it : c)
		cout << it << " ";

	if (paritate_a == 1 && paritate_b == 1)
		rezultat_final = (float)(c[c.size() / 2] + c[c.size() / 2 + 1]) / 2;
	
	if(paritate_a == 0 && paritate_b == 0)
		rezultat_final = (float)(c[c.size() / 2] + c[c.size() / 2 + 1]) / 2;

	if(paritate_a == 1 && paritate_b == 0)
		rezultat_final = (float)c[c.size() / 2];

	if(paritate_a == 0 && paritate_b == 1)
		rezultat_final = (float)c[c.size() / 2];
}

float mediana(vector <int> a, vector <int> b, int st_a, int st_b, int dr_a, int dr_b) {

	int paritateM1;
	int paritateM2;
	int pozM1;
	int pozM2;

	paritateM1 = (st_a + dr_a) % 2;
	if (paritateM1 == 0)
		pozM1 = (st_a + dr_a + 1) / 2;
	else
		pozM1 = (st_a + dr_a) / 2;

	paritateM2 = (st_b + dr_b) % 2;
	if (paritateM2 == 0)
		pozM2 = (st_b + dr_b + 1) / 2;
	else
		pozM2 = (st_b + dr_b) / 2;

	int m1 = a[pozM1];
	int m2 = b[pozM2];

	cout << st_a << " " << dr_a << " " << st_b << " " << dr_b << " ||| " << m1 << " " << m2 << " ||| " << pozM1 << " " << pozM2 << endl;

	if (m1 == m2)
		return (float)m1;
	
	if (dr_a - st_a + dr_b - st_b <= 5) {	//facem o interclasare de maxim 25 operatii
		obtinere_mediana(a, b, st_a, st_b, dr_a, dr_b, a.size() % 2, b.size() % 2);
		return rezultat_final;
	}
	
	if (m1 < m2) {
		mediana(a, b, pozM1, st_b, dr_a, pozM2);
	}
	else 
		if (m1 > m2) {
			mediana(a, b, st_a, pozM2, pozM1, dr_b);
		}

	return rezultat_final;
}

int main()
{
	ifstream fin("date.txt");
	ofstream fout("dateOut.txt");

	vector <int> a;
	vector <int> b;

	int na, nb;
	fin >> na;

	a.resize(na);
	for (int i = 0; i < na; i++) {
		int x;
		fin >> x;
		a[i] = x;
	}

	fin >> nb;
	b.resize(nb);
	for (int i = 0; i < nb; i++) {
		int x;
		fin >> x;
		b[i] = x;
	}

	if (a[na / 2] == b[nb / 2]) {
		fout << a[na / 2];
		return 0;
	}

	mediana(a, b, 0, 0, na - 1, nb - 1);
	cout << "\n \nMediana este: " << rezultat_final << endl;
	fout << rezultat_final;

	fin.close();
	fout.close();
	 
	return 0;
}