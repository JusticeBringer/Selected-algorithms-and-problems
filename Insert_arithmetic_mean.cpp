
#include "pch.h"
#include <stdlib.h>
#include <stdio.h>
#include <iostream>

using namespace std;

struct node
{
	int info;
	node* next;

}*first, *last;

typedef node* nod;

void adf(int x)
{
	if (last == NULL)
	{
		first = last = new node;
		last->info = x;
		last->next = NULL;
	}
	else
	{
		node* temporar = new node;
		temporar->info = x;
		temporar->next = NULL;
		last->next = temporar;
		last = temporar;

	}
}

void afisareLista()
{
	node* p = first;
	while (p != NULL)
	{
		cout << p->info<<" ";
		p = p->next;
		

	}
	cout << endl;
}

void inserareMedie()
{
	int medie=0;

	node *p = first;
	while (p->next != NULL)
	{
		medie = (p->info + p->next->info) / 2;
		node *temporar = new node;
		temporar->info = medie;
		temporar->next = p->next;
		p->next = temporar;
		p = p->next->next;
	}


}

int main()
{
	int n, i, x;

	printf("n=");
	cin>> n;;
	for (i = 0; i < n; i++)
	{
		cout << "x=";
		cin >> x;
		adf(x);
	}

	afisareLista();

	inserareMedie();
	afisareLista();

	return 0;

}