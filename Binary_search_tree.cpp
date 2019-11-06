#include "pch.h"
#include <iostream>

using namespace std;

struct arb
{
	int info;
	arb *st, *dr;
}*radacina;

typedef arb* nod;

nod insertie (nod curent, int x)
{
	if (curent == NULL)
	{
		nod temp = new arb;
		temp->info = x;
		temp->st = NULL;
		temp->dr = NULL;
		return temp;
	}
	else
	{
		if (x < curent->info)
			curent->st = insertie(curent->st, x);
		else
			curent->dr = insertie(curent->dr, x);

	}
	return curent;
}

void afisareInOrdine (nod curent) //SRD
{
	if (curent== NULL)
		return;
	
	afisareInOrdine(curent->st);
	cout << curent->info << " ";
	afisareInOrdine(curent->dr);

}

void afisarePreOrdine(nod curent) //RSD
{
	if (curent == NULL)
		return;

	cout << curent->info << " ";
	afisarePreOrdine(curent->st);
	afisarePreOrdine(curent->dr);
}

void afisarePostOrdine(nod curent)//SDR
{
	if (curent == NULL)
		return;

	afisarePostOrdine(curent->st);
	afisarePostOrdine(curent->dr);
	cout << curent->info << " ";

}

nod cauta(nod curent, int x)
{
	if (curent == NULL)
		return NULL;

	if (curent->info == x)
		return curent;

	if (x > curent->info)
		return cauta(curent->dr, x);

	return cauta(curent->st, x);
}

int max(nod curent, int x)
{
	int maxim = 0;

	if (curent->info > maxim)
		maxim = curent->info;

	if ((radacina->dr) != NULL)
		max(curent->dr, x);
	else
		return radacina->info;

	return maxim;
}

nod succesor(nod curent)
{
	curent = curent->dr;
	while (curent->st != NULL)
		curent = curent->st;
	
	return curent;
}

nod stergere(nod curent, int x)
{
	if (curent == NULL)
		return curent;
	
	//frunza
	if (x < curent->info)
		curent->st = stergere(curent->st, x);
	else
		if (x > curent->info)
			curent->dr = stergere(curent->dr, x);
		else
		{	//un fiu
			if (curent->dr == NULL && curent->st != NULL)
			{
				nod temp = curent->st;
				delete curent;
				return temp;
			
			}
			else
				if (curent->dr != NULL && curent->st == NULL)
				{
					nod temp = curent->dr;
					delete curent;
					return temp;
				}
				else
					// are ambii fii
				{
					nod temp = succesor(curent);
					curent->info = temp->info;
					curent->dr = stergere(curent->dr, temp->info);
				}

		}
	return curent;
}

int main()
{
	nod p = NULL;

	p =	insertie(p, 5);
	p = insertie(p, 2);
	p = insertie(p, 4);
	p = insertie(p, 3);
	p = insertie(p, 8);
	p = insertie(p, 6);
	p = insertie(p, 7);
	cout << endl;
	p = stergere(p, 5);
	afisarePreOrdine(p);

	return 0;
}

