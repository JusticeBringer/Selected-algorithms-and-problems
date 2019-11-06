#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <set>

using namespace std;

struct MyStruct
{
	string sir = "";
	int apar1 = 0;
	int apar2 = 0;
};

class Tema {
	protected:
		vector <string> cuv;
		static int nr;
		MyStruct final[100];

	public:
		Tema() {
			cuv.clear();
		}

		void add_One(string sir) {
			if (search(sir) == false) {
				nr++;
				cuv.push_back(sir);

				final[nr].apar1++;
				final[nr].apar2 = 0;
				final[nr].sir = sir;
			}
			else{
				final[return_Poz(sir)].apar1++;
			}
		}

		void add_Two(string sir) {
			if (search(sir) == false) {
				nr++;
				cuv.push_back(sir);

				final[nr].apar1 = 0;
				final[nr].apar2++;
				final[nr].sir = sir;
			}
			else {
				final[return_Poz(sir)].apar2++;
			}
		}

		int return_Poz(string sir) {
			int k = 0;
			for (auto it : cuv) {
				k++;
				if (it == sir)
					return k;
			}
			return -1;
		}

		bool search(string sir) {
			if (cuv.size() == 0)
				return false;
			for (auto it : cuv)
				if (it == sir)
					return true;
			return false;
		}

		void show_Cuv() {
			for (auto it : cuv)
				cout << it << " ";
		}

		void show_Struct() {
			for (int i = 1; i <= cuv.size(); i++) {
				cout << final[i].sir << " " << final[i].apar1 << " " << final[i].apar2 << endl;
			}
		}

		bool poti_Calcula() {
			int sum = 0;
			for (int i = 1; i <= nr; i++)
				sum += final[i].apar1;
			if (sum == 0)
				return false;

			for (int i = 1; i <= nr; i++) {
				sum += final[i].apar2;
			}
			if (sum == 0)
				return false;
			return true;
		}

		void cos_Dist() {
			if (poti_Calcula() == false) {
				cout << "Nu se poate calcula";
				return;
			}

			double numarator = 0;
			double numitor_Unu = 0;
			double numitor_Doi = 0;

			for (int i = 1; i <= nr; i++) {
				numarator += (double)final[i].apar1 * (double)final[i].apar2;
			}

			for (int i = 1; i <= nr; i++) {
				numitor_Unu += (double)final[i].apar1 * (double)final[i].apar1;
			}

			for (int i = 1; i <= nr; i++) {
				numitor_Doi += (double)final[i].apar2 * (double)final[i].apar2;
			}

			cout << numarator / (sqrt(numitor_Unu) * sqrt(numitor_Doi))	;
		}
};

int Tema::nr = 0;

int main()
{
	ifstream fin1("data1.txt");
	ifstream fin2("data2.txt");

	Tema T;

	string cuvant;
	while (fin1 >> cuvant){
		T.add_One(cuvant);
	}

	while (fin2 >> cuvant) {
		T.add_Two(cuvant);
	}

	T.show_Struct();
	T.cos_Dist();
}